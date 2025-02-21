"""PlanetaryGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6745,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6651
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6756,
        _6794,
        _6696,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundCriticalSpeedAnalysis")


class PlanetaryGearSetCompoundCriticalSpeedAnalysis(
    _6745.CylindricalGearSetCompoundCriticalSpeedAnalysis
):
    """PlanetaryGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
            parent: "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6745.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6745.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6756.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6696.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
        ) -> "PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "PlanetaryGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6651.PlanetaryGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PlanetaryGearSetCriticalSpeedAnalysis]

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
    ) -> "List[_6651.PlanetaryGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PlanetaryGearSetCriticalSpeedAnalysis]

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
    ) -> "PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis(self)
