"""StraightBevelSunGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5827
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelSunGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.system_deflections import _2828
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5703,
        _5691,
        _5720,
        _5761,
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearHarmonicAnalysis")


class StraightBevelSunGearHarmonicAnalysis(_5827.StraightBevelDiffGearHarmonicAnalysis):
    """StraightBevelSunGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearHarmonicAnalysis")

    class _Cast_StraightBevelSunGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelSunGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
            parent: "StraightBevelSunGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5827.StraightBevelDiffGearHarmonicAnalysis":
            return self._parent._cast(_5827.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5703.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5691.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5720.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5761.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
        ) -> "StraightBevelSunGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "_2828.StraightBevelSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection

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
    ) -> "StraightBevelSunGearHarmonicAnalysis._Cast_StraightBevelSunGearHarmonicAnalysis":
        return self._Cast_StraightBevelSunGearHarmonicAnalysis(self)
