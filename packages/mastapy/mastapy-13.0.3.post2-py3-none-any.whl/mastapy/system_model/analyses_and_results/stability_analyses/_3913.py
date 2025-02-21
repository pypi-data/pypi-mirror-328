"""WormGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "WormGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7006
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3914,
        _3912,
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="WormGearSetStabilityAnalysis")


class WormGearSetStabilityAnalysis(_3845.GearSetStabilityAnalysis):
    """WormGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetStabilityAnalysis")

    class _Cast_WormGearSetStabilityAnalysis:
        """Special nested class for casting WormGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
            parent: "WormGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
        ) -> "WormGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2572.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7006.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears_stability_analysis(
        self: Self,
    ) -> "List[_3914.WormGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3912.WormGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetStabilityAnalysis._Cast_WormGearSetStabilityAnalysis":
        return self._Cast_WormGearSetStabilityAnalysis(self)
