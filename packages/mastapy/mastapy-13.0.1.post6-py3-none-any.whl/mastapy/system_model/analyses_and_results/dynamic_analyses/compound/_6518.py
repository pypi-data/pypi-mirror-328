"""StraightBevelGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6426
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6516,
        _6517,
        _6414,
        _6442,
        _6468,
        _6506,
        _6408,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearSetCompoundDynamicAnalysis")


class StraightBevelGearSetCompoundDynamicAnalysis(
    _6426.BevelGearSetCompoundDynamicAnalysis
):
    """StraightBevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCompoundDynamicAnalysis"
    )

    class _Cast_StraightBevelGearSetCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
            parent: "StraightBevelGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6426.BevelGearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6442.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6468.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6506.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6408.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
        ) -> "StraightBevelGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2548.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6389.StraightBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6516.StraightBevelGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6517.StraightBevelGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6389.StraightBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis":
        return self._Cast_StraightBevelGearSetCompoundDynamicAnalysis(self)
