import sys
from inspect import signature
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    get_type_hints,
)
from collections.abc import Callable

from pydantic.alias_generators import to_pascal
from pydantic.functional_validators import field_validator
from pydantic.main import BaseModel, create_model

from .parameters import Signature

__all__ = ["ValidatedFunction"]

assert sys.version_info >= (3, 10), "typing.get_type_hints needs Python 3.10+"

if TYPE_CHECKING:
    AnyCallable = Callable[..., Any]

    AnyCallableT = TypeVar("AnyCallableT", bound=AnyCallable)


ALT_V_ARGS = "v__args"
ALT_V_KWARGS = "v__kwargs"
V_POSITIONAL_ONLY_NAME = "v__positional_only"
V_DUPLICATE_KWARGS = "v__duplicate_kwargs"


class ValidatedFunction:
    def __init__(self, function: "AnyCallable"):
        sig = signature(function)
        type_hints: dict[str, Any] = get_type_hints(function, include_extras=True)
        self.sig_model = Signature.model_validate(
            sig,
            from_attributes=True,
            context=type_hints,
        )
        self.source_name = function.__name__
        self.create_model(
            self.sig_model.fields,
            self.sig_model.takes_args,
            self.sig_model.takes_kwargs,
        )

    def build_values(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        values: dict[str, Any] = {}
        if args:
            arg_iter = enumerate(args)
            while True:
                try:
                    i, a = next(arg_iter)
                except StopIteration:
                    break
                arg_name = self.sig_model.arg_mapping.get(i)
                if arg_name is not None:
                    values[arg_name] = a
                else:
                    values[self.sig_model.v_args_name] = [a] + [a for _, a in arg_iter]
                    break

        var_kwargs: dict[str, Any] = {}
        wrong_positional_args = []
        duplicate_kwargs = []
        fields_alias = [
            field.alias
            for name, field in self.model.model_fields.items()
            if name not in (self.sig_model.v_args_name, self.sig_model.v_kwargs_name)
        ]
        non_var_fields = set(self.model.model_fields) - {
            self.sig_model.v_args_name,
            self.sig_model.v_kwargs_name,
        }
        for k, v in kwargs.items():
            if k in non_var_fields or k in fields_alias:
                if k in self.sig_model.positional_only_args:
                    wrong_positional_args.append(k)
                if k in values:
                    duplicate_kwargs.append(k)
                values[k] = v
            else:
                var_kwargs[k] = v

        if var_kwargs:
            values[self.sig_model.v_kwargs_name] = var_kwargs
        if wrong_positional_args:
            values[V_POSITIONAL_ONLY_NAME] = wrong_positional_args
        if duplicate_kwargs:
            values[V_DUPLICATE_KWARGS] = duplicate_kwargs
        return values

    def create_model(
        self,
        fields: dict[str, Any],
        takes_args: bool,
        takes_kwargs: bool,
    ) -> None:
        pos_args = len(self.sig_model.arg_mapping)

        class DecoratorBaseModel(BaseModel):
            @field_validator(self.sig_model.v_args_name, check_fields=False)
            @classmethod
            def check_args(cls, v: list[Any] | None) -> list[Any] | None:
                if takes_args or v is None:
                    return v

                raise TypeError(
                    f"{pos_args} positional arguments expected but {pos_args + len(v)} given",
                )

            @field_validator(self.sig_model.v_kwargs_name, check_fields=False)
            @classmethod
            def check_kwargs(
                cls,
                v: dict[str, Any] | None,
            ) -> dict[str, Any] | None:
                if takes_kwargs or v is None:
                    return v

                plural = "" if len(v) == 1 else "s"
                keys = ", ".join(map(repr, v.keys()))
                raise TypeError(f"unexpected keyword argument{plural}: {keys}")

            @field_validator(V_POSITIONAL_ONLY_NAME, check_fields=False)
            @classmethod
            def check_positional_only(cls, v: list[str] | None) -> None:
                if v is None:
                    return

                plural = "" if len(v) == 1 else "s"
                keys = ", ".join(map(repr, v))
                raise TypeError(
                    f"positional-only argument{plural} passed as keyword argument{plural}: {keys}",
                )

            @field_validator(V_DUPLICATE_KWARGS, check_fields=False)
            @classmethod
            def check_duplicate_kwargs(cls, v: list[str] | None) -> None:
                if v is None:
                    return

                plural = "" if len(v) == 1 else "s"
                keys = ", ".join(map(repr, v))
                raise TypeError(f"multiple values for argument{plural}: {keys}")

        self.model = create_model(
            to_pascal(self.source_name),
            __base__=DecoratorBaseModel,
            **fields,
        )
