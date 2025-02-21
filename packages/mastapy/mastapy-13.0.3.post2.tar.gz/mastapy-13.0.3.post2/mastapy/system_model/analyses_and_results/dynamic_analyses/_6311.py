"""BevelDifferentialGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelDifferentialGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6846
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6309,
        _6310,
        _6304,
        _6332,
        _6360,
        _6398,
        _6298,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetDynamicAnalysis")


class BevelDifferentialGearSetDynamicAnalysis(_6316.BevelGearSetDynamicAnalysis):
    """BevelDifferentialGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearSetDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
            parent: "BevelDifferentialGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6316.BevelGearSetDynamicAnalysis":
            return self._parent._cast(_6316.BevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6304.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6332.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6360.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6398.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6298.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
        ) -> "BevelDifferentialGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6846.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6309.BevelDifferentialGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6310.BevelDifferentialGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetDynamicAnalysis._Cast_BevelDifferentialGearSetDynamicAnalysis":
        return self._Cast_BevelDifferentialGearSetDynamicAnalysis(self)
