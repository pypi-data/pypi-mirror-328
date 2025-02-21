"""DatumSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "DatumSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6891
    from mastapy.system_model.analyses_and_results.power_flows import _4105
    from mastapy.system_model.analyses_and_results.system_deflections import _2806
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("DatumSystemDeflection",)


Self = TypeVar("Self", bound="DatumSystemDeflection")


class DatumSystemDeflection(_2736.ComponentSystemDeflection):
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
        ) -> "_2736.ComponentSystemDeflection":
            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumSystemDeflection._Cast_DatumSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2468.Datum":
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
    def component_load_case(self: Self) -> "_6891.DatumLoadCase":
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
    def power_flow_results(self: Self) -> "_4105.DatumPowerFlow":
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
