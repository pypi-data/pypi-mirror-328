# (generated with --quick)

from typing import Any, Iterable, NamedTuple, Union

class Message(NamedTuple):
    type: Any
    data: Any
    time: Any
    name: Any
    color: Any

class Printer:
    __doc__: str
    color: Any
    prefix: Any
    time_format: Any
    width: Any
    def __init__(self, print_func, time_format = ..., width = ..., color = ..., prefix = ...) -> None: ...
    def print_func(self, _1: str) -> Any: ...
    def write(self, message) -> None: ...

def _color_string(color, s) -> str: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, rename: bool = ..., defaults: list = ..., module = ...) -> type: ...
