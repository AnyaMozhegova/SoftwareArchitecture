from typing import Any, TypeVar, Callable, Set, List, Type

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int))
    return float(x)


def from_set(f: Callable[[Any], T], x: Any) -> Set[T]:
    assert isinstance(x, list)
    return {f(y) for y in x}


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return x.to_dict()

def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    """
    Преобразует список данных в список объектов типа T, применяя функцию f для каждого элемента.
    """
    assert isinstance(x, list)
    return [f(y) for y in x]