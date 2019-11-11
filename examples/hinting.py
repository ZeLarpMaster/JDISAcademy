from typing import Callable, Generator


def func(chaine: str, nombre: int) -> str:
    return chaine * nombre


YieldType = int
SendType = float
ReturnType = str


# Exemple pris de https://docs.python.org/3/library/typing.html#typing.Generator
def generator() -> Generator[YieldType, SendType, ReturnType]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return "Done"


def createur_de_callable() -> Callable[[int], int]:
    return lambda x: x


# Pour plus d'information: https://docs.python.org/3/library/typing.html
