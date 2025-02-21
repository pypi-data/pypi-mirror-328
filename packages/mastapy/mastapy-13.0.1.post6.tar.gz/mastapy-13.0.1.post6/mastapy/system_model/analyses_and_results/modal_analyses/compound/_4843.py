"""SynchroniserPartCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SynchroniserPartCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4699
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4842,
        _4844,
        _4805,
        _4753,
        _4807,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundModalAnalysis")


class SynchroniserPartCompoundModalAnalysis(_4767.CouplingHalfCompoundModalAnalysis):
    """SynchroniserPartCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundModalAnalysis"
    )

    class _Cast_SynchroniserPartCompoundModalAnalysis:
        """Special nested class for casting SynchroniserPartCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
            parent: "SynchroniserPartCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4767.CouplingHalfCompoundModalAnalysis":
            return self._parent._cast(_4767.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4805.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4842.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "_4844.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
        ) -> "SynchroniserPartCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4699.SynchroniserPartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4699.SynchroniserPartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundModalAnalysis._Cast_SynchroniserPartCompoundModalAnalysis":
        return self._Cast_SynchroniserPartCompoundModalAnalysis(self)
