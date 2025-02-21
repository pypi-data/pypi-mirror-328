"""CycloidalDiscCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6430
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CycloidalDiscCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2589
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6431,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundDynamicAnalysis")


class CycloidalDiscCompoundDynamicAnalysis(_6430.AbstractShaftCompoundDynamicAnalysis):
    """CycloidalDiscCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscCompoundDynamicAnalysis")

    class _Cast_CycloidalDiscCompoundDynamicAnalysis:
        """Special nested class for casting CycloidalDiscCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
            parent: "CycloidalDiscCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_6430.AbstractShaftCompoundDynamicAnalysis":
            return self._parent._cast(_6430.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_6431.AbstractShaftOrHousingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(
                _6431.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def component_compound_dynamic_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
        ) -> "CycloidalDiscCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_6343.CycloidalDiscDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscDynamicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6343.CycloidalDiscDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscDynamicAnalysis]

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
    ) -> "CycloidalDiscCompoundDynamicAnalysis._Cast_CycloidalDiscCompoundDynamicAnalysis":
        return self._Cast_CycloidalDiscCompoundDynamicAnalysis(self)
