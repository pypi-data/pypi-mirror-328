"""TorqueConverterTurbineAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TorqueConverterTurbineAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7353,
        _7298,
        _7355,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineAdvancedSystemDeflection")


class TorqueConverterTurbineAdvancedSystemDeflection(
    _7313.CouplingHalfAdvancedSystemDeflection
):
    """TorqueConverterTurbineAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineAdvancedSystemDeflection"
    )

    class _Cast_TorqueConverterTurbineAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
            parent: "TorqueConverterTurbineAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7313.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7313.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7353.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7298.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
        ) -> "TorqueConverterTurbineAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection",
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
        instance_to_wrap: "TorqueConverterTurbineAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2831.TorqueConverterTurbineSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineAdvancedSystemDeflection._Cast_TorqueConverterTurbineAdvancedSystemDeflection":
        return self._Cast_TorqueConverterTurbineAdvancedSystemDeflection(self)
