"""StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7117,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.system_deflections import _2819
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7027,
        _7014,
        _7043,
        _7069,
        _7089,
        _7036,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation(
    _7117.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7117.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7027.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7043.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "_2819.StraightBevelPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection

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
    ) -> "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
