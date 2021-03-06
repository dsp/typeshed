# Stubs for re
# Ron Murawski <ron@horizonchess.com>
# 'bytes' support added by Jukka Lehtosalo

# based on: http://docs.python.org/2.7/library/re.html

from typing import (
    List, Iterator, overload, Callable, Tuple, Sequence, Dict,
    Generic, AnyStr, Match, Pattern
)

# ----- re variables and constants -----
DEBUG = 0
I = 0
IGNORECASE = 0
L = 0
LOCALE = 0
M = 0
MULTILINE = 0
S = 0
DOTALL = 0
X = 0
VERBOSE = 0
U = 0
UNICODE = 0
T = 0
TEMPLATE = 0

class error(Exception): ...

def compile(pattern: AnyStr, flags: int = ...) -> Pattern[AnyStr]: ...
def search(pattern: AnyStr, string: AnyStr,
           flags: int = ...) -> Match[AnyStr]: ...
def match(pattern: AnyStr, string: AnyStr,
          flags: int = ...) -> Match[AnyStr]: ...
def split(pattern: AnyStr, string: AnyStr, maxsplit: int = ...,
          flags: int = ...) -> List[AnyStr]: ...
def findall(pattern: AnyStr, string: AnyStr,
            flags: int = ...) -> List[AnyStr]: ...

# Return an iterator yielding match objects over all non-overlapping matches
# for the RE pattern in string. The string is scanned left-to-right, and
# matches are returned in the order found. Empty matches are included in the
# result unless they touch the beginning of another match.
def finditer(pattern: AnyStr, string: AnyStr,
             flags: int = ...) -> Iterator[Match[AnyStr]]: ...

@overload
def sub(pattern: AnyStr, repl: AnyStr, string: AnyStr, count: int = ...,
        flags: int = ...) -> AnyStr: ...
@overload
def sub(pattern: AnyStr, repl: Callable[[Match[AnyStr]], AnyStr],
        string: AnyStr, count: int = ..., flags: int = ...) -> AnyStr: ...

@overload
def subn(pattern: AnyStr, repl: AnyStr, string: AnyStr, count: int = ...,
         flags: int = ...) -> Tuple[AnyStr, int]: ...
@overload
def subn(pattern: AnyStr, repl: Callable[[Match[AnyStr]], AnyStr],
         string: AnyStr, count: int = ...,
         flags: int = ...) -> Tuple[AnyStr, int]: ...

def escape(string: AnyStr) -> AnyStr: ...

def purge() -> None: ...
