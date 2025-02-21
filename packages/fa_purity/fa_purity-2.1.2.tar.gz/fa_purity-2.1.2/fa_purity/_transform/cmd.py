"""Common transforms utils/module over core types."""

from __future__ import (
    annotations,
)

from collections.abc import Callable
from dataclasses import (
    dataclass,
)
from typing import (
    TypeVar,
)

from fa_purity._core.cmd import (
    Cmd,
    CmdUnwrapper,
)
from fa_purity._core.frozen import (
    FrozenList,
)

_A = TypeVar("_A")
_B = TypeVar("_B")


Mapper = Callable[[Callable[[_A], _B], FrozenList[_A]], FrozenList[_B]]


@dataclass(frozen=True)
class CmdTransform:
    """Transform utils for `Cmd` instances."""

    @staticmethod
    def serial_merge(items: FrozenList[Cmd[_A]]) -> Cmd[FrozenList[_A]]:
        """
        Create a serial execution of commands.

        Create a new command that will execute the supplied commands
        in sequential order when computed.
        """

        def _action(unwrapper: CmdUnwrapper) -> FrozenList[_A]:
            return tuple(map(unwrapper.act, items))

        return Cmd.new_cmd(_action)
