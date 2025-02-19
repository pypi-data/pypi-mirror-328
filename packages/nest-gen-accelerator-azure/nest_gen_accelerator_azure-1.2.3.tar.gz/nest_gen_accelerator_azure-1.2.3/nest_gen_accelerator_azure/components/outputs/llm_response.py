import random
import traceback
from enum import Enum
from typing import Optional, Type

from promptflow._utils.logger_utils import flow_logger
from pydantic import BaseModel, ConfigDict, Field, field_serializer, model_validator

from nest_gen_accelerator_azure.components.output_parsers import JsonOutputParser
from nest_gen_accelerator_azure.components.outputs import BaseExitStrategy, CallToAction
from nest_gen_accelerator_azure.exceptions import (
    ContentPolicyViolationException,
    InvalidLLMResponseException,
)
from nest_gen_accelerator_azure.utils import _merge_enums


class ContentFilterResults(BaseModel):
    prompt_results: dict
    completion_results: dict


class LLMResponse(BaseModel):
    """LLMResponse class encapsulating the response structure and parsing logic."""

    content: str = Field(alias="content")
    call_to_action: CallToAction = Field(alias="callToAction")
    exit_strategy: Enum = Field(alias="exitStrategy")
    additional_exit_strategies: Optional[Type[Enum]] = Field(default=None)
    model_details: dict = Field(alias="modelStats", default_factory=dict)
    context: Optional[str] = Field(alias="context", default=None)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        protected_namespaces=(),
    )

    @model_validator(mode="before")
    @classmethod
    def validate_exit_strategy(cls, values):
        AdditionalExitStrategy: Optional[Type[Enum]] = values.pop(
            "additional_exit_strategies", None
        )

        if AdditionalExitStrategy:
            if not (
                isinstance(AdditionalExitStrategy, type)
                and issubclass(AdditionalExitStrategy, Enum)
            ):
                raise ValueError("additional_exit_strategies must be of type Enum")

            ExitStrategy = _merge_enums(
                BaseExitStrategy, AdditionalExitStrategy, "ExitStrategy"
            )
        else:
            ExitStrategy = BaseExitStrategy

        exit_strategy_value = None
        for key in ("exitStrategy", "exit_strategy"):
            if key in values:
                exit_strategy_value = values.pop(key)
                break

        if exit_strategy_value is None or exit_strategy_value == "":
            values["exit_strategy"] = BaseExitStrategy.EMPTY
            return values

        try:
            if isinstance(exit_strategy_value, Enum):
                exit_strategy = ExitStrategy(exit_strategy_value.value)
            elif isinstance(exit_strategy_value, str):
                exit_strategy = ExitStrategy(exit_strategy_value)
            else:
                raise ValueError(
                    f"Invalid type for exit_strategy: {type(exit_strategy_value)}. "
                    f"Must be a string or an Enum member."
                )
        except ValueError:
            raise InvalidLLMResponseException(
                f"Invalid exit_strategy: {exit_strategy_value}. "
                f"Must be one of {list(ExitStrategy)}"
            )

        values["exit_strategy"] = exit_strategy
        return values

    @field_serializer("call_to_action", when_used="json")
    def serialize_call_to_action(self, call_to_action: CallToAction) -> dict:
        return call_to_action.model_dump(exclude_none=True)

    @field_serializer("exit_strategy", when_used="json")
    def serialize_exit_strategy(self, exit_strategy: Enum) -> str:
        return exit_strategy.value

    @classmethod
    def _build_model_details(cls, llm_response: dict) -> dict:
        """Builds the model details from the LLM response."""
        content_filter_results = cls.parse_content_filter_results(llm_response)
        return {
            "name": llm_response.get("model", ""),
            "prompt_tokens": llm_response.get("usage", {}).get("prompt_tokens", None),
            "completion_tokens": llm_response.get("usage", {}).get(
                "completion_tokens", 0
            ),
            "total_tokens": llm_response.get("usage", {}).get("total_tokens", None),
            "params": llm_response.get("params", {}),
            "content_filter_results": content_filter_results.model_dump(),
        }

    @classmethod
    def validate_response_structure(cls, llm_response: dict) -> None:
        """Validates the LLM response structure has all required fields."""
        if not isinstance(llm_response, dict):
            raise InvalidLLMResponseException("LLM response must be a dictionary")

        # Check main required keys
        if not all(
            key in llm_response for key in ["choices", "model", "usage", "params"]
        ):
            raise InvalidLLMResponseException(
                "Missing required top-level keys in LLM response"
            )

        # Validate choices structure
        choices = llm_response.get("choices", [])
        if not choices or not isinstance(choices[0], dict):
            raise InvalidLLMResponseException("Invalid choices structure")

        # Validate message structure
        message = choices[0].get("message", {})
        if not isinstance(message, dict) or "content" not in message:
            raise InvalidLLMResponseException("Invalid message structure")

        # Validate usage structure
        usage = llm_response.get("usage", {})
        required_usage = ["prompt_tokens", "completion_tokens", "total_tokens"]
        if not all(key in usage for key in required_usage):
            raise InvalidLLMResponseException("Missing required usage statistics")

    @classmethod
    def create_error_response(
        cls,
        message: str,
        exit_strategy: BaseExitStrategy,
        llm_response: dict,
        context: Optional[str] = None,
    ) -> "LLMResponse":
        """Creates a standardized error response."""
        return cls(
            content=message,
            call_to_action=CallToAction(type="NONE"),
            exit_strategy=exit_strategy,
            model_details=(
                cls._build_model_details(llm_response) if llm_response else {}
            ),
            context=context,
        )

    @staticmethod
    def check_policy_violation(error_info: dict) -> None:
        """
        Checks content policy violations by raising an appropriate exception.

        Args:
            error_info: Dictionary containing error information.

        Raises:
            ContentPolicyViolationException: If a content policy violation is detected.
        """
        error = error_info.get("errorMessage", {}).get("error", {})
        if not error.get("code") == "content_filter":
            return

        raise ContentPolicyViolationException(error.get("message"), details=error)

    @classmethod
    def process_response_errors(cls, llm_response: dict) -> None:
        """Process any errors in the LLM response and raise appropriate exceptions."""
        error = llm_response.get("error", {})
        if not error:
            return

        response = error.get("response", {})

        cls.check_policy_violation(response)

        raise InvalidLLMResponseException(
            f"Error in LLM response ({error['type']}): {error['details']}"
        )

    @staticmethod
    def parse_content_filter_results(llm_response: dict) -> ContentFilterResults:
        """
        Parse content filter results from the LLM response.

        Args:
            llm_response: LLM response dictionary.

        Returns:
            ContentFilterResults: Content filter results.
        """
        prompt_results = {}
        completion_results = {}

        if "error" in llm_response:
            error = (
                llm_response["error"]
                .get("response", {})
                .get("errorMessage", {})
                .get("error", {})
            )
            trigger = error.get("param")
            content_filter_result = error.get("innererror", {}).get(
                "content_filter_result", {}
            )

            if trigger == "prompt":
                prompt_results = content_filter_result

            # TODO Determine how to handle completion content filter results

        else:
            prompt_filter_results = llm_response.get("prompt_filter_results", [{}])
            if prompt_filter_results:
                prompt_results = prompt_filter_results[0].get(
                    "content_filter_results", {}
                )
            else:
                prompt_results = {}

            choices = llm_response.get("choices", [{}])
            if choices:
                completion_results = choices[0].get("content_filter_results", {})
            else:
                completion_results = {}

        return ContentFilterResults(
            prompt_results=prompt_results, completion_results=completion_results
        )

    @classmethod
    def from_json(
        cls,
        llm_response: dict,
        tracking_id: str,
        *,
        additional_exit_strategies: Optional[Type[Enum]] = None,
        context: Optional[str] = None,
    ) -> "LLMResponse":
        try:
            cls.process_response_errors(llm_response)
            cls.validate_response_structure(llm_response)

            choices = llm_response["choices"]
            message = choices[0]["message"]
            message_content = JsonOutputParser.parse(message["content"])
            content = message_content.get("content")
            exit_strategy = message_content.get("exitStrategy")

            call_to_action = CallToAction(type="NONE")
            if not exit_strategy:
                
                model_call_to_action = message_content.get("callToAction", {}) if message_content else {}
                call_to_action = CallToAction(**model_call_to_action) if model_call_to_action else call_to_action

            model_details = cls._build_model_details(llm_response)

            response_instance = cls(
                content=content,
                call_to_action=call_to_action,
                additional_exit_strategies=additional_exit_strategies,
                exit_strategy=exit_strategy,
                model_details=model_details,
                context=context,
            )

            flow_logger.info(
                "Successfully parsed JSON response.",
                extra={
                    "content": content,
                    "tracking_id": tracking_id,
                    "total_tokens": model_details.get("total_tokens"),
                    "exit_strategy": exit_strategy,
                },
            )

            return response_instance

        except ContentPolicyViolationException as e:
            flow_logger.warning(
                "Content policy violation detected",
                extra={
                    "tracking_id": tracking_id,
                    "type": type(e).__name__,
                    "details": e.details,
                },
            )
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to content policy restrictions.",
                BaseExitStrategy.OUT_OF_DOMAIN,
                llm_response,
                context=context,
            )

        except InvalidLLMResponseException as e:
            flow_logger.error(
                f"Invalid LLM response structure: {e}. LLM response: {llm_response}",
                extra={"error": str(e), "tracking_id": tracking_id},
            )
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to an internal error.",
                BaseExitStrategy.ON_ERROR,
                llm_response,
                context=context,
            )

        except Exception as e:
            flow_logger.error(
                f"Unexpected error while parsing LLM response: {e}",
                extra={
                    "error": str(e),
                    "tracking_id": tracking_id,
                    "traceback": traceback.format_exc(),
                },
            )
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to an internal error.",
                BaseExitStrategy.ON_ERROR,
                llm_response,
                context=context,
            )

    def to_dict(self) -> dict:
        return self.model_dump(mode="json", by_alias=True)
