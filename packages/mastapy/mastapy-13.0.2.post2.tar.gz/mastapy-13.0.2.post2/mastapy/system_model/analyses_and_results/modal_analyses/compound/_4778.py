"""CVTPulleyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CVTPulleyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4623
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4775,
        _4813,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundModalAnalysis")


class CVTPulleyCompoundModalAnalysis(_4824.PulleyCompoundModalAnalysis):
    """CVTPulleyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundModalAnalysis")

    class _Cast_CVTPulleyCompoundModalAnalysis:
        """Special nested class for casting CVTPulleyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
            parent: "CVTPulleyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_4824.PulleyCompoundModalAnalysis":
            return self._parent._cast(_4824.PulleyCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_4775.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
        ) -> "CVTPulleyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4623.CVTPulleyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4623.CVTPulleyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis]

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
    ) -> "CVTPulleyCompoundModalAnalysis._Cast_CVTPulleyCompoundModalAnalysis":
        return self._Cast_CVTPulleyCompoundModalAnalysis(self)
