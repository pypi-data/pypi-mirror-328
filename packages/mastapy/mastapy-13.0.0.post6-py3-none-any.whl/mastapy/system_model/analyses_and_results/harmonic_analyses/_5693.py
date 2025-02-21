"""BevelDifferentialSunGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialSunGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.system_deflections import _2705
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5694,
        _5682,
        _5711,
        _5752,
        _5785,
        _5704,
        _5787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearHarmonicAnalysis")


class BevelDifferentialSunGearHarmonicAnalysis(
    _5689.BevelDifferentialGearHarmonicAnalysis
):
    """BevelDifferentialSunGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
            parent: "BevelDifferentialSunGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5689.BevelDifferentialGearHarmonicAnalysis":
            return self._parent._cast(_5689.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5694.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5682.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5711.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5752.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5785.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5704.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5787.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "BevelDifferentialSunGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2518.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2705.BevelDifferentialSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis":
        return self._Cast_BevelDifferentialSunGearHarmonicAnalysis(self)
