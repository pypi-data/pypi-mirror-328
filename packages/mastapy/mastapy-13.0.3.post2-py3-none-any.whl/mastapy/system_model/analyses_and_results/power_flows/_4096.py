"""CycloidalAssemblyPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4156
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CycloidalAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6879
    from mastapy.system_model.analyses_and_results.power_flows import _4053, _4135
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyPowerFlow",)


Self = TypeVar("Self", bound="CycloidalAssemblyPowerFlow")


class CycloidalAssemblyPowerFlow(_4156.SpecialisedAssemblyPowerFlow):
    """CycloidalAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyPowerFlow")

    class _Cast_CycloidalAssemblyPowerFlow:
        """Special nested class for casting CycloidalAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
            parent: "CycloidalAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_4053.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_power_flow(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
        ) -> "CycloidalAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6879.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblyPowerFlow._Cast_CycloidalAssemblyPowerFlow":
        return self._Cast_CycloidalAssemblyPowerFlow(self)
