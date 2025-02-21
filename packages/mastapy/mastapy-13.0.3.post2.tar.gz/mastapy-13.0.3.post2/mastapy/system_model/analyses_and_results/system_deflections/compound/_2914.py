"""CVTPulleyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CVTPulleyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2911,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleyCompoundSystemDeflection")


class CVTPulleyCompoundSystemDeflection(_2961.PulleyCompoundSystemDeflection):
    """CVTPulleyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundSystemDeflection")

    class _Cast_CVTPulleyCompoundSystemDeflection:
        """Special nested class for casting CVTPulleyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
            parent: "CVTPulleyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2961.PulleyCompoundSystemDeflection":
            return self._parent._cast(_2961.PulleyCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2911.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
        ) -> "CVTPulleyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2754.CVTPulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection]

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
    def component_analysis_cases(self: Self) -> "List[_2754.CVTPulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection]

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
    ) -> "CVTPulleyCompoundSystemDeflection._Cast_CVTPulleyCompoundSystemDeflection":
        return self._Cast_CVTPulleyCompoundSystemDeflection(self)
