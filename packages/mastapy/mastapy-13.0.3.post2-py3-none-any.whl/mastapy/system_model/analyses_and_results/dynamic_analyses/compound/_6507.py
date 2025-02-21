"""OilSealCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6465
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "OilSealCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6506,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="OilSealCompoundDynamicAnalysis")


class OilSealCompoundDynamicAnalysis(_6465.ConnectorCompoundDynamicAnalysis):
    """OilSealCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundDynamicAnalysis")

    class _Cast_OilSealCompoundDynamicAnalysis:
        """Special nested class for casting OilSealCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
            parent: "OilSealCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6465.ConnectorCompoundDynamicAnalysis":
            return self._parent._cast(_6465.ConnectorCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6506.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
        ) -> "OilSealCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.OilSeal":
        """mastapy.system_model.part_model.OilSeal

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
    ) -> "List[_6378.OilSealDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6378.OilSealDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis]

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
    ) -> "OilSealCompoundDynamicAnalysis._Cast_OilSealCompoundDynamicAnalysis":
        return self._Cast_OilSealCompoundDynamicAnalysis(self)
