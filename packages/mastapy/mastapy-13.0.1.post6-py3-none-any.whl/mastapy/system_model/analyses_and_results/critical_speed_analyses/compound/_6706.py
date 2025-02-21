"""ConceptGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6735,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6574
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6704,
        _6705,
        _6773,
        _6675,
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundCriticalSpeedAnalysis")


class ConceptGearSetCompoundCriticalSpeedAnalysis(
    _6735.GearSetCompoundCriticalSpeedAnalysis
):
    """ConceptGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConceptGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
            parent: "ConceptGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6735.GearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6675.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
        ) -> "ConceptGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_6574.ConceptGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearSetCriticalSpeedAnalysis]

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
    def concept_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6704.ConceptGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ConceptGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6705.ConceptGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ConceptGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6574.ConceptGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearSetCriticalSpeedAnalysis]

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
    ) -> "ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis(self)
