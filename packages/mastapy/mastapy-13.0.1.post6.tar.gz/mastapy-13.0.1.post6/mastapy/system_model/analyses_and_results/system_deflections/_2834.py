"""UnbalancedMassSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "UnbalancedMassSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.power_flows import _4159
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2782,
        _2715,
        _2785,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7547,
        _7548,
        _7545,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassSystemDeflection",)


Self = TypeVar("Self", bound="UnbalancedMassSystemDeflection")


class UnbalancedMassSystemDeflection(_2835.VirtualComponentSystemDeflection):
    """UnbalancedMassSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassSystemDeflection")

    class _Cast_UnbalancedMassSystemDeflection:
        """Special nested class for casting UnbalancedMassSystemDeflection to subclasses."""

        def __init__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            parent: "UnbalancedMassSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2835.VirtualComponentSystemDeflection":
            return self._parent._cast(_2835.VirtualComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2782.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2715.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2785.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "UnbalancedMassSystemDeflection":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6981.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4159.UnbalancedMassPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection":
        return self._Cast_UnbalancedMassSystemDeflection(self)
