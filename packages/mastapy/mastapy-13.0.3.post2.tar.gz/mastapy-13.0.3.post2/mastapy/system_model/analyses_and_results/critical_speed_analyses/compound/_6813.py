"""TorqueConverterCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6733,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6685
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6794,
        _6696,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterCompoundCriticalSpeedAnalysis")


class TorqueConverterCompoundCriticalSpeedAnalysis(
    _6733.CouplingCompoundCriticalSpeedAnalysis
):
    """TorqueConverterCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundCriticalSpeedAnalysis"
    )

    class _Cast_TorqueConverterCompoundCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
            parent: "TorqueConverterCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_critical_speed_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_6733.CouplingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6733.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_6696.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
        ) -> "TorqueConverterCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "TorqueConverterCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2628.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2628.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

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
    ) -> "List[_6685.TorqueConverterCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.TorqueConverterCriticalSpeedAnalysis]

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
    ) -> "List[_6685.TorqueConverterCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.TorqueConverterCriticalSpeedAnalysis]

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
    ) -> "TorqueConverterCompoundCriticalSpeedAnalysis._Cast_TorqueConverterCompoundCriticalSpeedAnalysis":
        return self._Cast_TorqueConverterCompoundCriticalSpeedAnalysis(self)
