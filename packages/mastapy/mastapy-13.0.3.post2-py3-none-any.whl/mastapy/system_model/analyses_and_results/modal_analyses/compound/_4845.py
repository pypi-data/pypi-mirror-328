"""ShaftHubConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ShaftHubConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2619
    from mastapy.system_model.analyses_and_results.modal_analyses import _4699
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4826,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundModalAnalysis")


class ShaftHubConnectionCompoundModalAnalysis(_4785.ConnectorCompoundModalAnalysis):
    """ShaftHubConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionCompoundModalAnalysis"
    )

    class _Cast_ShaftHubConnectionCompoundModalAnalysis:
        """Special nested class for casting ShaftHubConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
            parent: "ShaftHubConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_modal_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_4785.ConnectorCompoundModalAnalysis":
            return self._parent._cast(_4785.ConnectorCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
        ) -> "ShaftHubConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2619.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

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
    ) -> "List[_4699.ShaftHubConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftHubConnectionCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftHubConnectionCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4699.ShaftHubConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis]

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
    ) -> "ShaftHubConnectionCompoundModalAnalysis._Cast_ShaftHubConnectionCompoundModalAnalysis":
        return self._Cast_ShaftHubConnectionCompoundModalAnalysis(self)
