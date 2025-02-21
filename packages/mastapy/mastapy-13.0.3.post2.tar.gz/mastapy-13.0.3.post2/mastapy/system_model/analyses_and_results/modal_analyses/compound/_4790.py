"""CVTCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CVTCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4635
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4847,
        _4749,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundModalAnalysis")


class CVTCompoundModalAnalysis(_4759.BeltDriveCompoundModalAnalysis):
    """CVTCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundModalAnalysis")

    class _Cast_CVTCompoundModalAnalysis:
        """Special nested class for casting CVTCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
            parent: "CVTCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4759.BeltDriveCompoundModalAnalysis":
            return self._parent._cast(_4759.BeltDriveCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4847.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis",
        ) -> "CVTCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4635.CVTModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_4635.CVTModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis]

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
    ) -> "CVTCompoundModalAnalysis._Cast_CVTCompoundModalAnalysis":
        return self._Cast_CVTCompoundModalAnalysis(self)
