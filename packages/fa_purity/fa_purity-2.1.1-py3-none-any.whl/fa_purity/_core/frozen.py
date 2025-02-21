"""Frozen module."""

from __future__ import (
    annotations,
)

from collections.abc import Callable, ItemsView, Iterator, Mapping
from dataclasses import (
    dataclass,
)
from typing import (
    Generic,
    TypeVar,
    overload,
)

_K = TypeVar("_K")
_V = TypeVar("_V")
_T = TypeVar("_T")
_A = TypeVar("_A")
_B = TypeVar("_B")

FrozenList = tuple[_T, ...]  # type: ignore[misc]


@dataclass(frozen=True)
class _FrozenDict(Generic[_K, _V]):
    _dict: dict[_K, _V]


class FrozenDict(Mapping[_K, _V], _FrozenDict[_K, _V]):
    """Frozen equivalent to builtin `Dict`."""

    def __init__(self, dictionary: dict[_K, _V]) -> None:
        super().__init__(dictionary.copy())

    def __getitem__(self, key: _K) -> _V:
        return self._dict[key]

    def __iter__(self) -> Iterator[_K]:
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)

    def __str__(self) -> str:
        return self.__class__.__name__ + str(self._dict)

    def __repr__(self) -> str:
        return self.__class__.__name__ + str(self._dict)

    def __hash__(self) -> int:
        return hash(frozenset(self._dict.items()))

    @staticmethod
    def from_items(
        items: ItemsView[_K, _V] | FrozenList[tuple[_K, _V]],
    ) -> FrozenDict[_K, _V]:
        """Build a `FrozenDict` from a list/view of key-value pairs."""
        return FrozenDict(dict(items))

    def map(self, keys: Callable[[_K], _A], values: Callable[[_V], _B]) -> FrozenDict[_A, _B]:
        """
        Transform keys and values.

        Create a new `FrozenDict` where each key and value gets transformed.
        """
        return FrozenDict({keys(k): values(v) for k, v in self.items()})


@dataclass(frozen=True)
class FrozenTools:
    @staticmethod
    def chain(unchained: FrozenList[FrozenList[_T]]) -> FrozenList[_T]:
        return tuple(item for items in unchained for item in items)

    @overload
    @staticmethod
    def freeze(target: list[_T]) -> FrozenList[_T]:
        pass

    @overload
    @staticmethod
    def freeze(target: dict[_K, _V]) -> FrozenDict[_K, _V]:
        pass

    @staticmethod
    def freeze(
        target: list[_T] | dict[_K, _V],
    ) -> FrozenList[_T] | FrozenDict[_K, _V]:
        if isinstance(target, list):
            return tuple(target)
        return FrozenDict(target)

    @overload
    @staticmethod
    def unfreeze(target: FrozenList[_T]) -> list[_T]:
        pass

    @overload
    @staticmethod
    def unfreeze(target: FrozenDict[_K, _V]) -> dict[_K, _V]:
        pass

    @staticmethod
    def unfreeze(
        target: FrozenList[_T] | FrozenDict[_K, _V],
    ) -> list[_T] | dict[_K, _V]:
        if isinstance(target, FrozenDict):
            return dict(target.items())
        return list(target)
