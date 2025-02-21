"""ElectricMachineStatorToothTangentialLoadsExcitationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_TANGENTIAL_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5754,
        _5813,
        _5700,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothTangentialLoadsExcitationDetail",)


Self = TypeVar(
    "Self", bound="ElectricMachineStatorToothTangentialLoadsExcitationDetail"
)


class ElectricMachineStatorToothTangentialLoadsExcitationDetail(
    _5761.ElectricMachineStatorToothLoadsExcitationDetail
):
    """ElectricMachineStatorToothTangentialLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_TANGENTIAL_LOADS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    )

    class _Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothTangentialLoadsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
            parent: "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ) -> "_5761.ElectricMachineStatorToothLoadsExcitationDetail":
            return self._parent._cast(
                _5761.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ) -> "_5754.ElectricMachinePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ) -> "_5813.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ) -> "_5700.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
        ) -> "ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothTangentialLoadsExcitationDetail._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothTangentialLoadsExcitationDetail(
            self
        )
