"""PlanetaryGearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6457
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PlanetaryGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6468,
        _6506,
        _6408,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundDynamicAnalysis")


class PlanetaryGearSetCompoundDynamicAnalysis(
    _6457.CylindricalGearSetCompoundDynamicAnalysis
):
    """PlanetaryGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundDynamicAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundDynamicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
            parent: "PlanetaryGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6457.CylindricalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(_6457.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6468.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6506.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6408.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
        ) -> "PlanetaryGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6363.PlanetaryGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6363.PlanetaryGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis]

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
    ) -> "PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis":
        return self._Cast_PlanetaryGearSetCompoundDynamicAnalysis(self)
