"""CylindricalPlanetGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3834
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3846,
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearStabilityAnalysis")


class CylindricalPlanetGearStabilityAnalysis(_3834.CylindricalGearStabilityAnalysis):
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
        ) -> "_3834.CylindricalGearStabilityAnalysis":
            return self._parent._cast(_3834.CylindricalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    ) -> "CylindricalPlanetGearStabilityAnalysis._Cast_CylindricalPlanetGearStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearStabilityAnalysis(self)
