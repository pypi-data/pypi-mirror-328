"""WoundFieldSynchronousMachine"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WOUND_FIELD_SYNCHRONOUS_MACHINE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WoundFieldSynchronousMachine"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1292, _1279


__docformat__ = "restructuredtext en"
__all__ = ("WoundFieldSynchronousMachine",)


Self = TypeVar("Self", bound="WoundFieldSynchronousMachine")


class WoundFieldSynchronousMachine(_1304.NonCADElectricMachineDetail):
    """WoundFieldSynchronousMachine

    This is a mastapy class.
    """

    TYPE = _WOUND_FIELD_SYNCHRONOUS_MACHINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WoundFieldSynchronousMachine")

    class _Cast_WoundFieldSynchronousMachine:
        """Special nested class for casting WoundFieldSynchronousMachine to subclasses."""

        def __init__(
            self: "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine",
            parent: "WoundFieldSynchronousMachine",
        ):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(
            self: "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine",
        ) -> "_1304.NonCADElectricMachineDetail":
            return self._parent._cast(_1304.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(
            self: "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine",
        ) -> "_1279.ElectricMachineDetail":
            from mastapy.electric_machines import _1279

            return self._parent._cast(_1279.ElectricMachineDetail)

        @property
        def wound_field_synchronous_machine(
            self: "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine",
        ) -> "WoundFieldSynchronousMachine":
            return self._parent

        def __getattr__(
            self: "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WoundFieldSynchronousMachine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(
        self: Self,
    ) -> "_1292.InteriorPermanentMagnetAndSynchronousReluctanceRotor":
        """mastapy.electric_machines.InteriorPermanentMagnetAndSynchronousReluctanceRotor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine":
        return self._Cast_WoundFieldSynchronousMachine(self)
