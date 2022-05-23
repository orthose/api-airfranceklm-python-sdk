from typing import List, Dict
from enum import Enum


def names_from_enums(list_enum: List[Enum]) -> List[str]:
    return list(map(lambda x: x.name, list_enum))

def dicts_from_objs(list_objs: List) -> List[Dict]:
    return list(map(lambda x: x.to_dict(), list_objs))
