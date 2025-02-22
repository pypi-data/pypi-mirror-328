"""
This module implements an RGB color class, that can be instantiated from a HEX string.
"""

from dataclasses import dataclass


@dataclass
class RGBColor:
    r: int
    g: int
    b: int

    @classmethod
    def from_hex(cls, value: str) -> "RGBColor":
        value = value.lstrip("#")

        if len(value) == 6:
            col_len = 2
            mult = 1
        elif len(value) == 3:
            col_len = 1
            mult = 17
        else:
            raise ValueError(f"Color HEX strings may either have 3 or 6 characters. Got {len(value)} instead.")

        r, g, b = (
            int(value[:col_len], 16) * mult,
            int(value[col_len:2 * col_len], 16) * mult,
            int(value[2 * col_len:], 16) * mult
        )

        return cls(r, g, b)

    def __str__(self):
        return str((self.r, self.g, self.b))

    def __repr__(self):
        return f"{self.__class__.__name__}{self}"
