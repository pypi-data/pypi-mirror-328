"""CouplingPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4063,
        _4068,
        _4125,
        _4149,
        _4164,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingPowerFlow",)


Self = TypeVar("Self", bound="CouplingPowerFlow")


class CouplingPowerFlow(_4143.SpecialisedAssemblyPowerFlow):
    """CouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingPowerFlow")

    class _Cast_CouplingPowerFlow:
        """Special nested class for casting CouplingPowerFlow to subclasses."""

        def __init__(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
            parent: "CouplingPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4063.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4068.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConceptCouplingPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4125.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PartToPartShearCouplingPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4149.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SpringDamperPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4164.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.TorqueConverterPowerFlow)

        @property
        def coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "CouplingPowerFlow":
            return self._parent

        def __getattr__(self: "CouplingPowerFlow._Cast_CouplingPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingPowerFlow._Cast_CouplingPowerFlow":
        return self._Cast_CouplingPowerFlow(self)
