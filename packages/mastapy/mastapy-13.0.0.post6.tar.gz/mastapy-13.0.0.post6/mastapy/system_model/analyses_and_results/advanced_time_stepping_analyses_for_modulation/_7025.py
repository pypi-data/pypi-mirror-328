"""BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7021,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.system_deflections import _2705
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7026,
        _7013,
        _7042,
        _7068,
        _7088,
        _7035,
        _7090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"
)


class BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation(
    _7021.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7021.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7021.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7026.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7013.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7013,
            )

            return self._parent._cast(
                _7013.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7068.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation(
            self
        )
