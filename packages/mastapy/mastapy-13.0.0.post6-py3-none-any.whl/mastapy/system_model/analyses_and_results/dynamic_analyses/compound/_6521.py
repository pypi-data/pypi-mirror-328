"""SynchroniserHalfCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6522
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SynchroniserHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6446,
        _6484,
        _6432,
        _6486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundDynamicAnalysis")


class SynchroniserHalfCompoundDynamicAnalysis(
    _6522.SynchroniserPartCompoundDynamicAnalysis
):
    """SynchroniserHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundDynamicAnalysis"
    )

    class _Cast_SynchroniserHalfCompoundDynamicAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
            parent: "SynchroniserHalfCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_6522.SynchroniserPartCompoundDynamicAnalysis":
            return self._parent._cast(_6522.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_6446.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_6484.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_6432.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_6486.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
        ) -> "SynchroniserHalfCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_6392.SynchroniserHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis]

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
    ) -> "List[_6392.SynchroniserHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis]

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
    ) -> "SynchroniserHalfCompoundDynamicAnalysis._Cast_SynchroniserHalfCompoundDynamicAnalysis":
        return self._Cast_SynchroniserHalfCompoundDynamicAnalysis(self)
