"""WormGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "WormGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7006
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6690,
        _6691,
        _6665,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="WormGearSetCriticalSpeedAnalysis")


class WormGearSetCriticalSpeedAnalysis(_6627.GearSetCriticalSpeedAnalysis):
    """WormGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetCriticalSpeedAnalysis")

    class _Cast_WormGearSetCriticalSpeedAnalysis:
        """Special nested class for casting WormGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
            parent: "WormGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_critical_speed_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_6627.GearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6627.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
        ) -> "WormGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetCriticalSpeedAnalysis.TYPE"):
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
    def worm_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6690.WormGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.WormGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6691.WormGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.WormGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetCriticalSpeedAnalysis._Cast_WormGearSetCriticalSpeedAnalysis":
        return self._Cast_WormGearSetCriticalSpeedAnalysis(self)
