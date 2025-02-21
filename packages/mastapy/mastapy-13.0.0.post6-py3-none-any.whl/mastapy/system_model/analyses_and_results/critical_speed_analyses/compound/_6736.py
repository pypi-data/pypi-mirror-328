"""HypoidGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6678,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "HypoidGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6706,
        _6732,
        _6751,
        _6699,
        _6753,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="HypoidGearCompoundCriticalSpeedAnalysis")


class HypoidGearCompoundCriticalSpeedAnalysis(
    _6678.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
):
    """HypoidGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_HypoidGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting HypoidGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
            parent: "HypoidGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6678.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6678.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6706.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6732.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6751.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6699.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "HypoidGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

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
    ) -> "List[_6607.HypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearCriticalSpeedAnalysis]

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
    ) -> "List[_6607.HypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearCriticalSpeedAnalysis]

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
    ) -> "HypoidGearCompoundCriticalSpeedAnalysis._Cast_HypoidGearCompoundCriticalSpeedAnalysis":
        return self._Cast_HypoidGearCompoundCriticalSpeedAnalysis(self)
