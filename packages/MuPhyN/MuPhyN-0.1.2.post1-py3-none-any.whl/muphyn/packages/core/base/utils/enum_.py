from enum import Enum

class Enum(Enum):

    @classmethod
    def keys(cls):
        return list(map(lambda c: c, cls))
    
    @classmethod
    def items(cls):
        return {c: c.value  for c in cls}

    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))