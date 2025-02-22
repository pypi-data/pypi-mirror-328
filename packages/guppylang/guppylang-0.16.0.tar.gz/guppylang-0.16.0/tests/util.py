from __future__ import annotations

from typing import TYPE_CHECKING, Any

from hugr.package import FuncDefnPointer, ModulePointer

import guppylang
from guppylang.module import GuppyModule

if TYPE_CHECKING:
    from hugr import Hugr

    from guppylang.definition.function import RawFunctionDef

    try:
        from tket2.circuit import (
            Tk2Circuit,  # type: ignore[import-untyped, import-not-found, unused-ignore]
        )
    except ImportError:
        Tk2Circuit = Any


def compile_guppy(fn) -> FuncDefnPointer:
    """A decorator that combines @guppy with HUGR compilation.

    Creates a temporary module that only contains the defined function.
    """
    assert not isinstance(
        fn,
        GuppyModule,
    ), "`@compile_guppy` does not support extra arguments."

    module = GuppyModule("module")
    defn = guppylang.decorator.guppy(module)(fn)
    return defn.compile()


def dump_llvm(hugr: Hugr | ModulePointer):
    # TODO: Support multiple modules?
    if isinstance(hugr, ModulePointer):
        hugr = hugr.module

    try:
        from execute_llvm import compile_module_to_string

        hugr_json = hugr.to_json()
        llvm_module = compile_module_to_string(hugr_json)
        print(llvm_module)  # noqa: T201

    except ImportError:
        pass


def guppy_to_circuit(guppy_func: RawFunctionDef) -> Tk2Circuit:
    """Convert a Guppy function definition to a `Tk2Circuit`."""
    # TODO: Should this be part of the guppy API?
    from tket2.circuit import Tk2Circuit

    module = guppy_func.id.module
    assert module is not None, "Function definition must belong to a module"

    hugr = module.compile()
    assert hugr is not None, "Module must be compilable"

    json = hugr.to_json()
    return Tk2Circuit.from_guppy_json(json, guppy_func.name)
