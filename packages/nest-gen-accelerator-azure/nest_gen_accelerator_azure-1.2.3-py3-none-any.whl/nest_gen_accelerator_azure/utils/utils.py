from enum import Enum
from itertools import chain


def _merge_enums(first: Enum, second: Enum, name: str) -> Enum:
    MergedEnum = Enum(name, [(i.name, i.value) for i in chain(first, second)])

    return MergedEnum
