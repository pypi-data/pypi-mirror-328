"""PowerLoadCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PowerLoadCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6485,
        _6433,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCompoundDynamicAnalysis")


class PowerLoadCompoundDynamicAnalysis(_6530.VirtualComponentCompoundDynamicAnalysis):
    """PowerLoadCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCompoundDynamicAnalysis")

    class _Cast_PowerLoadCompoundDynamicAnalysis:
        """Special nested class for casting PowerLoadCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
            parent: "PowerLoadCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_6530.VirtualComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6530.VirtualComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_6485.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_6433.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
        ) -> "PowerLoadCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_6366.PowerLoadDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6366.PowerLoadDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis]

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
    ) -> "PowerLoadCompoundDynamicAnalysis._Cast_PowerLoadCompoundDynamicAnalysis":
        return self._Cast_PowerLoadCompoundDynamicAnalysis(self)
