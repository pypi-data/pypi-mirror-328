"""FaceGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6735,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6728,
        _6729,
        _6773,
        _6675,
        _6754,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetCompoundCriticalSpeedAnalysis")


class FaceGearSetCompoundCriticalSpeedAnalysis(
    _6735.GearSetCompoundCriticalSpeedAnalysis
):
    """FaceGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_FaceGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FaceGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
            parent: "FaceGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6735.GearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6675.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6754.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
        ) -> "FaceGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2529.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

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
    ) -> "List[_6601.FaceGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FaceGearSetCriticalSpeedAnalysis]

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
    def face_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6728.FaceGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.FaceGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6729.FaceGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.FaceGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6601.FaceGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FaceGearSetCriticalSpeedAnalysis]

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
    ) -> "FaceGearSetCompoundCriticalSpeedAnalysis._Cast_FaceGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_FaceGearSetCompoundCriticalSpeedAnalysis(self)
