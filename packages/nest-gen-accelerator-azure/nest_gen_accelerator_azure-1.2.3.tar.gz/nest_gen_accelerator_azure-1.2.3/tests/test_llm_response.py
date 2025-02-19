from enum import Enum

import pytest

from nest_gen_accelerator_azure.components.output_parsers import JsonOutputParser
from nest_gen_accelerator_azure.components.outputs import BaseExitStrategy
from nest_gen_accelerator_azure.components.outputs.llm_response import LLMResponse
from nest_gen_accelerator_azure.exceptions import InvalidLLMResponseException


class AdditionalExitStrategy(Enum):
    ORDER = "ORDER"


@pytest.fixture
def valid_llm_response():
    return {
        "choices": [
            {
                "message": {
                    "content": '{"content": "Do you know where my orders FR6A0889826 and FR6A0898073 are?", "callToAction": {"type": "NONE"}, "exitStrategy": ""}'
                }
            }
        ],
        "model": "test-model",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        },
        "params": {"seed": 42, "temperature": 0.7},
    }


@pytest.fixture
def handover_response():
    return {
        "choices": [
            {
                "message": {
                    "content": '{"content": "Can I talk to an agent?", "callToAction": {"type": "TO_LIVE_AGENT", "value": true}, "exitStrategy": ""}'
                }
            }
        ],
        "model": "test-model",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        },
        "params": {"seed": 42, "temperature": 0.7},
    }


@pytest.fixture
def invalid_llm_response():
    return {
        "choices": [],
        "model": "test-model",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        },
        "params": {"seed": 42, "temperature": 0.7},
    }


@pytest.fixture
def policy_violation_response():
    return {
        "error": {
            "type": "HTTP error",
            "details": "400 Client Error: Bad Request",
            "response": {
                "errorCode": 400,
                "errorType": "HTTP:BAD_REQUEST",
                "errorMessage": {
                    "error": {
                        "message": "The response was filtered due to the triggering of content management policy.",
                        "type": None,
                        "param": "prompt",
                        "code": "content_filter",
                        "status": 400,
                        "innererror": {
                            "code": "ResponsibleAIPolicyViolation",
                            "content_filter_result": {
                                "hate": {"filtered": False, "severity": "safe"},
                                "jailbreak": {"filtered": False, "detected": False},
                                "self_harm": {"filtered": False, "severity": "safe"},
                                "sexual": {"filtered": False, "severity": "safe"},
                                "violence": {"filtered": True, "severity": "medium"},
                            },
                        },
                    }
                },
            },
            "status_code": 400,
        },
        "params": {},
    }


@pytest.fixture
def error_response():
    return {
        "error": {
            "type": "HTTP error",
            "details": "500 Server Error: Internal Server Error",
            "response": {"error": "Internal Server Error"},
            "status_code": 500,
        }
    }


class TestValidResponses:
    def test_from_json_valid_response(self, valid_llm_response):
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(
            valid_llm_response, tracking_id, context=context
        )

        assert (
            response.content
            == "Do you know where my orders FR6A0889826 and FR6A0898073 are?"
        )
        assert response.call_to_action.type == "NONE"
        assert response.exit_strategy == BaseExitStrategy.EMPTY
        assert response.model_details["name"] == "test-model"
        assert response.model_details["total_tokens"] == 30
        assert response.model_details["params"] == {"seed": 42, "temperature": 0.7}
        assert (
            response.model_details["content_filter_results"]["prompt_results"]
            is not None
        )
        assert (
            response.model_details["content_filter_results"]["completion_results"]
            is not None
        )
        assert response.context == context

    def test_from_json_handover_response(self, handover_response):
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(
            handover_response, tracking_id, context=context
        )

        assert response.call_to_action.type == "TO_LIVE_AGENT" 
        assert response.exit_strategy == BaseExitStrategy.EMPTY
        assert response.model_details["name"] == "test-model"
        assert response.model_details["total_tokens"] == 30
        assert response.context == context

    def test_to_json_serialization(self):
        valid_llm_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "Do you know where my orders FR6A0889826 and FR6A0898073 are?", "callToAction": {"type": "NONE"}, "exitStrategy": ""}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(
            valid_llm_response, tracking_id, context=context
        )
        serialized = response.to_dict()

        assert isinstance(serialized, dict)
        assert (
            serialized["content"]
            == "Do you know where my orders FR6A0889826 and FR6A0898073 are?"
        )
        assert serialized["callToAction"] == {"type": "NONE"}
        assert serialized["exitStrategy"] == ""
        assert serialized["modelStats"] == {
            "name": "test-model",
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
            "params": {"seed": 42, "temperature": 0.7},
            "content_filter_results": {
                "prompt_results": {},
                "completion_results": {},
            },
        }
        assert serialized["context"] == context

    def test_from_json_minimal_response(self):
        minimal_llm_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "This is a minimal response", "callToAction": {"type": "NONE"}, "exitStrategy": ""}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            },
            "params": {},
        }
        tracking_id = "test-tracking-id"
        response = LLMResponse.from_json(minimal_llm_response, tracking_id)

        assert response.content == "This is a minimal response"
        assert response.call_to_action.type == "NONE"
        assert response.exit_strategy == BaseExitStrategy.EMPTY
        assert response.model_details["name"] == "test-model"
        assert response.model_details["total_tokens"] == 0
        assert response.model_details["params"] == {}
        assert response.model_details["content_filter_results"] == {
            "prompt_results": {},
            "completion_results": {},
        }
        assert response.context is None


class TestErrorHandling:
    def test_from_json_invalid_response(self):
        invalid_llm_response = {
            "choices": [],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(
            invalid_llm_response, tracking_id, context=context
        )

        assert response.call_to_action.type == "NONE"
        assert response.exit_strategy == BaseExitStrategy.ON_ERROR
        assert response.model_details["name"] == "test-model"
        assert response.model_details["total_tokens"] == 30
        assert response.context == context

    def test_from_json_parsing_error(self, mocker):
        valid_llm_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "Do you know where my orders FR6A0889826 and FR6A0898073 are?", "callToAction": {"type": "NONE"}, "exitStrategy": ""}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"
        context = "test-context"
        mocker.patch.object(
            JsonOutputParser, "parse", side_effect=ValueError("Parsing error")
        )

        response = LLMResponse.from_json(
            valid_llm_response, tracking_id, context=context
        )

        assert response.call_to_action.type == "NONE"
        assert response.exit_strategy == BaseExitStrategy.ON_ERROR
        assert response.model_details["name"] == "test-model"
        assert response.model_details["total_tokens"] == 30
        assert (
            not response.model_details["content_filter_results"]["prompt_results"]
            and not response.model_details["content_filter_results"][
                "completion_results"
            ]
        )
        assert response.context == context

    def test_content_policy_violation(self):
        policy_violation_response = {
            "error": {
                "type": "HTTP error",
                "details": "400 Client Error: Bad Request",
                "response": {
                    "errorCode": 400,
                    "errorType": "HTTP:BAD_REQUEST",
                    "errorMessage": {
                        "error": {
                            "message": "The response was filtered due to the triggering of content management policy.",
                            "type": None,
                            "param": "prompt",
                            "code": "content_filter",
                            "status": 400,
                            "innererror": {
                                "code": "ResponsibleAIPolicyViolation",
                                "content_filter_result": {
                                    "hate": {"filtered": False, "severity": "safe"},
                                    "jailbreak": {"filtered": False, "detected": False},
                                    "self_harm": {
                                        "filtered": False,
                                        "severity": "safe",
                                    },
                                    "sexual": {"filtered": False, "severity": "safe"},
                                    "violence": {
                                        "filtered": True,
                                        "severity": "medium",
                                    },
                                },
                            },
                        }
                    },
                },
                "status_code": 400,
            },
            "params": {},
        }
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(
            policy_violation_response, tracking_id, context=context
        )

        assert response.call_to_action.type == "NONE"
        assert response.exit_strategy == BaseExitStrategy.OUT_OF_DOMAIN
        assert (
            response.model_details["content_filter_results"]["prompt_results"]
            is not None
        )
        assert response.model_details["content_filter_results"]["prompt_results"] == {
            "hate": {"filtered": False, "severity": "safe"},
            "jailbreak": {"filtered": False, "detected": False},
            "self_harm": {"filtered": False, "severity": "safe"},
            "sexual": {"filtered": False, "severity": "safe"},
            "violence": {"filtered": True, "severity": "medium"},
        }
        assert (
            response.model_details["content_filter_results"]["completion_results"] == {}
        )
        assert response.context == context

    def test_error_response(self):
        error_response = {
            "error": {
                "type": "HTTP error",
                "details": "500 Server Error: Internal Server Error",
                "response": {"error": "Internal Server Error"},
                "status_code": 500,
            }
        }
        tracking_id = "test-tracking-id"
        context = "test-context"
        response = LLMResponse.from_json(error_response, tracking_id, context=context)

        assert response.exit_strategy == BaseExitStrategy.ON_ERROR
        assert response.model_details["total_tokens"] is None
        assert (
            not response.model_details["content_filter_results"]["prompt_results"]
            and not response.model_details["content_filter_results"][
                "completion_results"
            ]
        )
        assert response.context == context


class TestExitStrategyValidation:
    def test_base_exit_strategy(self):
        base_exit_strategy_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "Test content", "callToAction": {"type": "NONE"}, "exitStrategy": "OUT_OF_DOMAIN"}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"
        response = LLMResponse.from_json(
            base_exit_strategy_response, tracking_id, additional_exit_strategies=None
        )
        assert response.exit_strategy == BaseExitStrategy.OUT_OF_DOMAIN

    def test_additional_exit_strategy(self):
        additional_exit_strategy_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "Test content", "callToAction": {"type": "NONE"}, "exitStrategy": "ORDER"}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"
        response = LLMResponse.from_json(
            additional_exit_strategy_response,
            tracking_id,
            additional_exit_strategies=AdditionalExitStrategy,
        )
        assert (
            response.exit_strategy.value == AdditionalExitStrategy.ORDER.value
        )  # ExitStrategy Enum is built from scratch and therefore a different class with extended values

    def test_non_existent_exit_strategy(self):
        non_existent_exit_strategy_response = {
            "choices": [
                {
                    "message": {
                        "content": '{"content": "Test content", "callToAction": {"type": "NONE"}, "exitStrategy": "NON_EXISTENT"}'
                    }
                }
            ],
            "model": "test-model",
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 20,
                "total_tokens": 30,
            },
            "params": {"seed": 42, "temperature": 0.7},
        }
        tracking_id = "test-tracking-id"

        response = LLMResponse.from_json(
            non_existent_exit_strategy_response,
            tracking_id,
            additional_exit_strategies=AdditionalExitStrategy,
        )
        assert response.exit_strategy == BaseExitStrategy.ON_ERROR

    def test_constructor_empty_string_exit_strategy(self):
        response = LLMResponse(
            content="Test content",
            callToAction={"type": "NONE"},
            exitStrategy="",
        )
        assert response.exit_strategy == BaseExitStrategy.EMPTY
