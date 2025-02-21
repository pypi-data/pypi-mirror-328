"""MomentInputComponent"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_INPUT_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.VaryingInputComponents", "MomentInputComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("MomentInputComponent",)


Self = TypeVar("Self", bound="MomentInputComponent")


class MomentInputComponent(_96.AbstractVaryingInputComponent):
    """MomentInputComponent

    This is a mastapy class.
    """

    TYPE = _MOMENT_INPUT_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MomentInputComponent")

    class _Cast_MomentInputComponent:
        """Special nested class for casting MomentInputComponent to subclasses."""

        def __init__(
            self: "MomentInputComponent._Cast_MomentInputComponent",
            parent: "MomentInputComponent",
        ):
            self._parent = parent

        @property
        def abstract_varying_input_component(
            self: "MomentInputComponent._Cast_MomentInputComponent",
        ) -> "_96.AbstractVaryingInputComponent":
            return self._parent._cast(_96.AbstractVaryingInputComponent)

        @property
        def moment_input_component(
            self: "MomentInputComponent._Cast_MomentInputComponent",
        ) -> "MomentInputComponent":
            return self._parent

        def __getattr__(
            self: "MomentInputComponent._Cast_MomentInputComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MomentInputComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def moment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @moment.setter
    @enforce_parameter_types
    def moment(self: Self, value: "float"):
        self.wrapped.Moment = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "MomentInputComponent._Cast_MomentInputComponent":
        return self._Cast_MomentInputComponent(self)
