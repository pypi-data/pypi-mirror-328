"""
Based on the colorama package by Jonathan Hartley.
Cf. https://pypi.org/project/colorama/
"""
import colorama
from colorama.ansi import CSI, AnsiCodes

from coloform.color import RGBColor


# redefine code_to_chars function to enable handling complex ansi codes
def code_to_chars(*args):
    parameter_string = ";".join([str(arg) for arg in args])
    return CSI + parameter_string + "m"


# monkey patch code_to_chars function
colorama.ansi.code_to_chars = code_to_chars


class TrueColorCodes:
    def __init__(self, signifier):
        self.signifier = signifier

    _ALIASES = {
        "BLACK": "HEX_000000",
        "RED": "HEX_FF0000",
        "GREEN": "HEX_00FF00",
        "BLUE": "HEX_0000FF",
        "YELLOW": "HEX_FFFF00",
        "CYAN": "HEX_00FFFF",
        "MAGENTA": "HEX_FF00FF",
        "WHITE": "HEX_FFFFFF"
    }

    # added for auto completion
    # yes, this is a stupid way to do it
    # now get off my back
    BLACK = ...
    RED = ...
    GREEN = ...
    BLUE = ...
    YELLOW = ...
    CYAN = ...
    MAGENTA = ...
    WHITE = ...
    RESET = ...

    def _reset(self):
        return code_to_chars(self.signifier + 1)

    def _from_index(self, n: int) -> str:
        return code_to_chars(self.signifier, 5, n)

    def from_rgb(self, r: int, g: int, b: int) -> str:
        return code_to_chars(self.signifier, 2, r, g, b)

    def from_hex(self, value: str) -> str:
        col = RGBColor.from_hex(value)
        return self.from_rgb(col.r, col.g, col.b)

    def _from_rgb_string(self, rgb_string: str):
        col_parts = rgb_string.split("_")[1:]
        cols = [int(col) for col in col_parts]
        return self.from_rgb(*cols)

    def _from_hex_string(self, hex_string: str):
        return self.from_hex(hex_string.split("_")[1])

    def __getattribute__(self, item: str):
        if item.startswith("_"):
            # fall back to __getattr__ for private stuff
            raise AttributeError

        if item in self._ALIASES:
            return self._from_hex_string(self._ALIASES[item])

        if item.startswith("RGB_"):
            return self._from_rgb_string(item)
        elif item.startswith("HEX_"):
            return self._from_hex_string(item)
        elif item == "RESET":
            return self._reset()
        else:
            raise AttributeError

    def __getattr__(self, item):
        # fall back to __dict__ lookup
        return super().__getattribute__(item)


class TrueColorFore(TrueColorCodes):
    def __init__(self):
        super().__init__(38)


class TrueColorBack(TrueColorCodes):
    def __init__(self):
        super().__init__(48)


class TrueColorUnder(TrueColorCodes):
    def __init__(self):
        super().__init__(58)


class ANSIRichStyle(AnsiCodes):
    BOLD = 1
    BRIGHT = 1
    FAINT = 2
    DIM = 2
    RESET_WEIGHT = 22
    NORMAL = 22

    ITALIC = 3
    ITALICS = 3
    RESET_ITALIC = 23
    RESET_ITALICS = 23

    UNDERLINE = 4
    UNDERLINED = 4
    DOUBLE_UNDERLINE = 21
    DOUBLE_UNDERLINED = 21
    RESET_UNDERLINE = 24
    RESET_UNDERLINED = 24

    FRAME = 51
    FRAMED = 51
    ENCIRCLE = 52
    ENCIRCLED = 52
    RESET_FRAME = 54
    RESET_FRAMED = 54
    RESET_ENCIRCLE = 54
    RESET_ENCIRCLED = 54

    OVERLINE = 53
    OVERLINED = 53
    RESET_OVERLINE = 55
    RESET_OVERLINED = 55

    BLINK = 5
    BLINK_FAST = 6
    RESET_BLINK = 25

    INVERT = 7
    RESET_INVERT = 27

    STRIKE_OUT = 9
    RESET_STRIKE_OUT = 29

    SUPERSCRIPT = 73
    SUBSCRIPT = 74
    RESET_SUPERSCRIPT = 75
    RESET_SUBSCRIPT = 75

    RESET_FG = 39
    RESET_BG = 49
    RESET_ALL = 0

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.RESET_ALL)


Fore = TrueColorFore()
Back = TrueColorBack()
Under = TrueColorUnder()
Style = ANSIRichStyle()
