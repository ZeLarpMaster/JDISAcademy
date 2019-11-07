from typing import Callable, Generator


def func(thing: str, num: int) -> str:
    return thing * num


YieldType = int
SendType = float
ReturnType = str


# Example taken from https://docs.python.org/3/library/typing.html#typing.Generator
def generator() -> Generator[YieldType, SendType, ReturnType]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return "Done"


def callback_maker() -> Callable[[int], int]:
    return lambda x: x


# Pour plus d'information: https://docs.python.org/3/library/typing.html
