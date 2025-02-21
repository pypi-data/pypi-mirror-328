"""RingPinsCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "RingPinsCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2590
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundSystemDeflection",)


Self = TypeVar("Self", bound="RingPinsCompoundSystemDeflection")


class RingPinsCompoundSystemDeflection(
    _2950.MountableComponentCompoundSystemDeflection
):
    """RingPinsCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsCompoundSystemDeflection")

    class _Cast_RingPinsCompoundSystemDeflection:
        """Special nested class for casting RingPinsCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
            parent: "RingPinsCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_compound_system_deflection(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
        ) -> "RingPinsCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2815.RingPinsSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_2815.RingPinsSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsCompoundSystemDeflection._Cast_RingPinsCompoundSystemDeflection":
        return self._Cast_RingPinsCompoundSystemDeflection(self)
