from enum import Enum


class BaseExitStrategy(Enum):
    OUT_OF_DOMAIN = "OUT_OF_DOMAIN"
    EMPTY = ""
    ON_ERROR = "ON_ERROR"
    CONVERSATION_STALLED = "CONVERSATION_STALLED"