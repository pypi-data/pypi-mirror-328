"""CylindricalPlanetGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6625,
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCriticalSpeedAnalysis")


class CylindricalPlanetGearCriticalSpeedAnalysis(
    _6614.CylindricalGearCriticalSpeedAnalysis
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
        ) -> "_6614.CylindricalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6614.CylindricalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6625.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCriticalSpeedAnalysis._Cast_CylindricalPlanetGearCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2547.CylindricalPlanetGear":
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
