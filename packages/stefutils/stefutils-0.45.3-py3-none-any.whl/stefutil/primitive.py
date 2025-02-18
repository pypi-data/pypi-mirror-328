"""
primitive manipulation
"""

import re
import math
from typing import List, Any, Union

__all__ = [
    'nan',
    'is_int', 'float_is_sci', 'is_float', 'float_is_int', 'clean_whitespace', 'get_substr_indices'
]


nan = float('nan')


def is_int(x: Any, allow_str: bool = False) -> bool:
    if allow_str and isinstance(x, str):
        try:
            x = int(x)
        except ValueError:
            return False
    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())


def float_is_sci(f: Union[float, str]) -> bool:
    return 'e' in str(f).lower()


def is_float(x: Any, no_int=False, no_sci=False) -> bool:
    try:
        f = float(x)
        is_int_ = f.is_integer()
        out = True
        if no_int:
            out = out and (not is_int_)
        if no_sci:
            out = out and (not float_is_sci(x))
        return out
    except (ValueError, TypeError):
        return False


def float_is_int(f: float, eps: float = None) -> Union[int, bool]:
    if eps:
        return f.is_integer() or math.isclose(f, round(f), abs_tol=eps)
    else:
        return f.is_integer()


def clean_whitespace(s: str):
    if not hasattr(clean_whitespace, 'pattern_space'):
        clean_whitespace.pattern_space = re.compile(r'\s+')
    return clean_whitespace.pattern_space.sub(' ', s).strip()


def get_substr_indices(s: str, s_sub: str) -> List[int]:
    s_sub = re.escape(s_sub)
    return [m.start() for m in re.finditer(s_sub, s)]


if __name__ == '__main__':
    def check_int():
        print(is_int(1))
        print(is_int(1.0))
        print(is_int(1.1))
        print(is_int('1'))
        print(is_int('1.0'))
        print(is_int('1.1'))
        print(is_int('1.1', allow_str=True))
        print(is_int('1.0', allow_str=True))
        print(is_int('1', allow_str=True))
        print(is_int('1.1', allow_str=False))
        print(is_int('1.0', allow_str=False))
        print(is_int('1', allow_str=False))
    check_int()
