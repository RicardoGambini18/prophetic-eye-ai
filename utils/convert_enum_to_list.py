from enum import Enum


def convert_enum_to_list(enum: Enum):
  return [member.value for member in enum.__members__.values()]
