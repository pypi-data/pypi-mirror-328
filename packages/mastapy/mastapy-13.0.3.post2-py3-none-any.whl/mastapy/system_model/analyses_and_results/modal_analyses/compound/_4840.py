"""RollingRingAssemblyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "RollingRingAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.modal_analyses import _4695
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4749,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundModalAnalysis")


class RollingRingAssemblyCompoundModalAnalysis(
    _4847.SpecialisedAssemblyCompoundModalAnalysis
):
    """RollingRingAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCompoundModalAnalysis"
    )

    class _Cast_RollingRingAssemblyCompoundModalAnalysis:
        """Special nested class for casting RollingRingAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
            parent: "RollingRingAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_4847.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4847.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
        ) -> "RollingRingAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

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
    ) -> "List[_4695.RollingRingAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis]

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
    ) -> "List[_4695.RollingRingAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis]

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
    ) -> "RollingRingAssemblyCompoundModalAnalysis._Cast_RollingRingAssemblyCompoundModalAnalysis":
        return self._Cast_RollingRingAssemblyCompoundModalAnalysis(self)
