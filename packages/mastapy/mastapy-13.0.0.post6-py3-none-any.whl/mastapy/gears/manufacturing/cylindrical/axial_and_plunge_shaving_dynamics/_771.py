"""ShavingDynamicsViewModelBase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsViewModelBase",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _754,
        _760,
        _770,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsViewModelBase",)


Self = TypeVar("Self", bound="ShavingDynamicsViewModelBase")


class ShavingDynamicsViewModelBase(_628.GearManufacturingConfigurationViewModel):
    """ShavingDynamicsViewModelBase

    This is a mastapy class.
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingDynamicsViewModelBase")

    class _Cast_ShavingDynamicsViewModelBase:
        """Special nested class for casting ShavingDynamicsViewModelBase to subclasses."""

        def __init__(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
            parent: "ShavingDynamicsViewModelBase",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_628.GearManufacturingConfigurationViewModel":
            return self._parent._cast(_628.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_754.ConventionalShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _754,
            )

            return self._parent._cast(_754.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_760.PlungeShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _760,
            )

            return self._parent._cast(_760.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_770.ShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _770,
            )

            return self._parent._cast(_770.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "ShavingDynamicsViewModelBase":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingDynamicsViewModelBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase":
        return self._Cast_ShavingDynamicsViewModelBase(self)
