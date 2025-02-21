from enum import StrEnum


class BlockType(StrEnum):
    IMPORT = "import"
    FUNCTION = "function"
    CLASS = "class"
    VALUE = "value"
    COMMENT = "comment"
    OTHER = "other"
