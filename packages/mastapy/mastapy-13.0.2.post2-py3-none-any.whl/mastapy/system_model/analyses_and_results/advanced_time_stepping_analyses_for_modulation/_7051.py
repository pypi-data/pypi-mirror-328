"""ConicalGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7077,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.system_deflections import _2734
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7022,
        _7030,
        _7033,
        _7034,
        _7035,
        _7082,
        _7086,
        _7089,
        _7092,
        _7119,
        _7125,
        _7128,
        _7131,
        _7132,
        _7146,
        _7097,
        _7044,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConicalGearAdvancedTimeSteppingAnalysisForModulation")


class ConicalGearAdvancedTimeSteppingAnalysisForModulation(
    _7077.GearAdvancedTimeSteppingAnalysisForModulation
):
    """ConicalGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConicalGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.GearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7077.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7030.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7033.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7034.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7119.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7128.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7132.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConicalGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConicalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2734.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

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
    ) -> "ConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConicalGearAdvancedTimeSteppingAnalysisForModulation(self)
