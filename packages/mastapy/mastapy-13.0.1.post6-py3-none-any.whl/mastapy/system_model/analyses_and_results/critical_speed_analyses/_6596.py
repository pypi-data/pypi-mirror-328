"""CylindricalPlanetGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6604,
        _6623,
        _6568,
        _6625,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCriticalSpeedAnalysis")


class CylindricalPlanetGearCriticalSpeedAnalysis(
    _6593.CylindricalGearCriticalSpeedAnalysis
):
    """CylindricalPlanetGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCriticalSpeedAnalysis"
    )

    class _Cast_CylindricalPlanetGearCriticalSpeedAnalysis:
        """Special nested class for casting CylindricalPlanetGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
            parent: "CylindricalPlanetGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6593.CylindricalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6593.CylindricalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6604.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6623.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6568.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6625.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "CylindricalPlanetGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis":
        return self._Cast_CylindricalPlanetGearCriticalSpeedAnalysis(self)
