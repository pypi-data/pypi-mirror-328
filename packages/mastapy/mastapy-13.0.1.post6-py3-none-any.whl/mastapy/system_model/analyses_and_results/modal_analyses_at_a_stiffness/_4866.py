"""BeltConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4923,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BeltConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4897,
        _4892,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BeltConnectionModalAnalysisAtAStiffness")


class BeltConnectionModalAnalysisAtAStiffness(
    _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
):
    """BeltConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_BeltConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting BeltConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
            parent: "BeltConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4923.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4892.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4897.CVTBeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
        ) -> "BeltConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BeltConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6821.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionModalAnalysisAtAStiffness._Cast_BeltConnectionModalAnalysisAtAStiffness":
        return self._Cast_BeltConnectionModalAnalysisAtAStiffness(self)
