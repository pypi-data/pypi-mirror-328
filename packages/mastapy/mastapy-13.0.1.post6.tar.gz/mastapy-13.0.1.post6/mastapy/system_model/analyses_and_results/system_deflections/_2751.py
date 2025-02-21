"""DatumSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2715
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "DatumSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.power_flows import _4084
    from mastapy.system_model.analyses_and_results.system_deflections import _2785
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7547,
        _7548,
        _7545,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("DatumSystemDeflection",)


Self = TypeVar("Self", bound="DatumSystemDeflection")


class DatumSystemDeflection(_2715.ComponentSystemDeflection):
    """DatumSystemDeflection

    This is a mastapy class.
    """

    TYPE = _DATUM_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumSystemDeflection")

    class _Cast_DatumSystemDeflection:
        """Special nested class for casting DatumSystemDeflection to subclasses."""

        def __init__(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
            parent: "DatumSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2715.ComponentSystemDeflection":
            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2785.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_system_deflection(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "DatumSystemDeflection":
            return self._parent

        def __getattr__(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2448.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6870.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4084.DatumPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.DatumPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DatumSystemDeflection._Cast_DatumSystemDeflection":
        return self._Cast_DatumSystemDeflection(self)
