"""TorqueConverterCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "TorqueConverterCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.stability_analyses import _3887
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3995,
        _3897,
        _3976,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterCompoundStabilityAnalysis")


class TorqueConverterCompoundStabilityAnalysis(_3934.CouplingCompoundStabilityAnalysis):
    """TorqueConverterCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundStabilityAnalysis"
    )

    class _Cast_TorqueConverterCompoundStabilityAnalysis:
        """Special nested class for casting TorqueConverterCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
            parent: "TorqueConverterCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_stability_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_3934.CouplingCompoundStabilityAnalysis":
            return self._parent._cast(_3934.CouplingCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_3995.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_3897.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3897,
            )

            return self._parent._cast(_3897.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_3976.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
        ) -> "TorqueConverterCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.TorqueConverter":
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
    def assembly_design(self: Self) -> "_2607.TorqueConverter":
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
    ) -> "List[_3887.TorqueConverterStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.TorqueConverterStabilityAnalysis]

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
    ) -> "List[_3887.TorqueConverterStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.TorqueConverterStabilityAnalysis]

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
    ) -> "TorqueConverterCompoundStabilityAnalysis._Cast_TorqueConverterCompoundStabilityAnalysis":
        return self._Cast_TorqueConverterCompoundStabilityAnalysis(self)
