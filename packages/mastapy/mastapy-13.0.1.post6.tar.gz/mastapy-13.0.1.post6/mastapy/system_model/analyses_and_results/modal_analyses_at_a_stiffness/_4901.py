"""CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4881,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4956,
        _4860,
        _4892,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness"
)


class CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness(
    _4881.CoaxialConnectionModalAnalysisAtAStiffness
):
    """CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
            parent: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4881.CoaxialConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4881.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4956.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(
                _4956.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4860,
            )

            return self._parent._cast(
                _4860.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_4892.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness(
                self
            )
        )
