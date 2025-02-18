from typing import TypeAlias, Protocol


class ColorValue(Protocol):
    """General color annotation, using `__str__` protocol"""

    def __str__(self) -> str: ...


ColorCode: TypeAlias = int | str
HexCode: TypeAlias = str
