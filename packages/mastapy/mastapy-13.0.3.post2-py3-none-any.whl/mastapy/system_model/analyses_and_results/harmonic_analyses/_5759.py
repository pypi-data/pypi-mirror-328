"""ElectricMachineRotorZForcePeriodicExcitationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5754
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Z_FORCE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5813, _5700


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineRotorZForcePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineRotorZForcePeriodicExcitationDetail")


class ElectricMachineRotorZForcePeriodicExcitationDetail(
    _5754.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineRotorZForcePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Z_FORCE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineRotorZForcePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachineRotorZForcePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorZForcePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
            parent: "ElectricMachineRotorZForcePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
        ) -> "_5754.ElectricMachinePeriodicExcitationDetail":
            return self._parent._cast(_5754.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
        ) -> "_5813.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
        ) -> "_5700.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
        ) -> "ElectricMachineRotorZForcePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail",
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
        instance_to_wrap: "ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineRotorZForcePeriodicExcitationDetail._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail":
        return self._Cast_ElectricMachineRotorZForcePeriodicExcitationDetail(self)
