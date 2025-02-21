"""CylindricalPlanetGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3825,
        _3842,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearStabilityAnalysis")


class CylindricalPlanetGearStabilityAnalysis(_3813.CylindricalGearStabilityAnalysis):
    """CylindricalPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearStabilityAnalysis"
    )

    class _Cast_CylindricalPlanetGearStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
            parent: "CylindricalPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3813.CylindricalGearStabilityAnalysis":
            return self._parent._cast(_3813.CylindricalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3825.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "CylindricalPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearStabilityAnalysis.TYPE"
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
    ) -> "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearStabilityAnalysis(self)
