"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6476
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6480,
        _6481,
        _6442,
        _6468,
        _6506,
        _6408,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis(
    _6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6442.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6468.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6506.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6408.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

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
    ) -> "List[_6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_dynamic_analysis(
        self: Self,
    ) -> "List[_6480.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundDynamicAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_dynamic_analysis(
        self: Self,
    ) -> (
        "List[_6481.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]"
    ):
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundDynamicAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis(
            self
        )
