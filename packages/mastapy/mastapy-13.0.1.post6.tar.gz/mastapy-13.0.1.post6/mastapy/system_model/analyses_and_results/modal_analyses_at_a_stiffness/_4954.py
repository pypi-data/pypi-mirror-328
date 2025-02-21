"""ShaftHubConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4893,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ShaftHubConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6950
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4936,
        _4882,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ShaftHubConnectionModalAnalysisAtAStiffness")


class ShaftHubConnectionModalAnalysisAtAStiffness(
    _4893.ConnectorModalAnalysisAtAStiffness
):
    """ShaftHubConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_ShaftHubConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting ShaftHubConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
            parent: "ShaftHubConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4893.ConnectorModalAnalysisAtAStiffness":
            return self._parent._cast(_4893.ConnectorModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4936.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4882.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
        ) -> "ShaftHubConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.ShaftHubConnection":
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
    def component_load_case(self: Self) -> "_6950.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftHubConnectionModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionModalAnalysisAtAStiffness._Cast_ShaftHubConnectionModalAnalysisAtAStiffness":
        return self._Cast_ShaftHubConnectionModalAnalysisAtAStiffness(self)
