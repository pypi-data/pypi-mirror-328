"""BevelDifferentialGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6422,
        _6423,
        _6412,
        _6440,
        _6466,
        _6485,
        _6433,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundDynamicAnalysis")


class BevelDifferentialGearCompoundDynamicAnalysis(
    _6424.BevelGearCompoundDynamicAnalysis
):
    """BevelDifferentialGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
            parent: "BevelDifferentialGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6424.BevelGearCompoundDynamicAnalysis":
            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6412.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6440.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6466.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6485.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6433.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6422.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(
                _6422.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "_6423.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
        ) -> "BevelDifferentialGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6288.BevelDifferentialGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6288.BevelDifferentialGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearCompoundDynamicAnalysis._Cast_BevelDifferentialGearCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialGearCompoundDynamicAnalysis(self)
