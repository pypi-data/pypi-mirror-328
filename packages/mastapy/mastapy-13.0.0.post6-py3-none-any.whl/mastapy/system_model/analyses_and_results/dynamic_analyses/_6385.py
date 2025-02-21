"""StraightBevelDiffGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelDiffGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6383,
        _6384,
        _6282,
        _6310,
        _6338,
        _6376,
        _6276,
        _6357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetDynamicAnalysis")


class StraightBevelDiffGearSetDynamicAnalysis(_6294.BevelGearSetDynamicAnalysis):
    """StraightBevelDiffGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetDynamicAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
            parent: "StraightBevelDiffGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6294.BevelGearSetDynamicAnalysis":
            return self._parent._cast(_6294.BevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6282.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6310.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6338.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6376.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6276.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_6357.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "StraightBevelDiffGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6961.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6383.StraightBevelDiffGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6384.StraightBevelDiffGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis":
        return self._Cast_StraightBevelDiffGearSetDynamicAnalysis(self)
