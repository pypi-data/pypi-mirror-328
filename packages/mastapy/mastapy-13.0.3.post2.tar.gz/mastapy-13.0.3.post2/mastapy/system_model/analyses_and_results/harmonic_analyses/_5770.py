"""FaceGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "FaceGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.static_loads import _6908
    from mastapy.system_model.analyses_and_results.system_deflections import _2776
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5768,
        _5769,
        _5831,
        _5699,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetHarmonicAnalysis")


class FaceGearSetHarmonicAnalysis(_5779.GearSetHarmonicAnalysis):
    """FaceGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetHarmonicAnalysis")

    class _Cast_FaceGearSetHarmonicAnalysis:
        """Special nested class for casting FaceGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
            parent: "FaceGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_5779.GearSetHarmonicAnalysis":
            return self._parent._cast(_5779.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_5831.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_5699.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
        ) -> "FaceGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2549.FaceGearSet":
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
    def assembly_load_case(self: Self) -> "_6908.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2776.FaceGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(self: Self) -> "List[_5768.FaceGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5768.FaceGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5769.FaceGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5769.FaceGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetHarmonicAnalysis._Cast_FaceGearSetHarmonicAnalysis":
        return self._Cast_FaceGearSetHarmonicAnalysis(self)
