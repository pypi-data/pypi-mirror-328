"""HypoidGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6680,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6736,
        _6737,
        _6708,
        _6734,
        _6772,
        _6674,
        _6753,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundCriticalSpeedAnalysis")


class HypoidGearSetCompoundCriticalSpeedAnalysis(
    _6680.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
):
    """HypoidGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_HypoidGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting HypoidGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
            parent: "HypoidGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6680.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6680.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6734.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6772.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6674.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6674,
            )

            return self._parent._cast(
                _6674.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6753.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
        ) -> "HypoidGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2535.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6609.HypoidGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6736.HypoidGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.HypoidGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6737.HypoidGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.HypoidGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6609.HypoidGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCompoundCriticalSpeedAnalysis._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_HypoidGearSetCompoundCriticalSpeedAnalysis(self)
