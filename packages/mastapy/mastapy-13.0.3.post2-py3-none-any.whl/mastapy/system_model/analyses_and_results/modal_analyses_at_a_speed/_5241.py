"""SpringDamperConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.static_loads import _6978
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5203,
        _5173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperConnectionModalAnalysisAtASpeed")


class SpringDamperConnectionModalAnalysisAtASpeed(
    _5175.CouplingConnectionModalAnalysisAtASpeed
):
    """SpringDamperConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionModalAnalysisAtASpeed"
    )

    class _Cast_SpringDamperConnectionModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
            parent: "SpringDamperConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_5175.CouplingConnectionModalAnalysisAtASpeed":
            return self._parent._cast(_5175.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_5203.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(
                _5203.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_5173.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
        ) -> "SpringDamperConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2370.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6978.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionModalAnalysisAtASpeed._Cast_SpringDamperConnectionModalAnalysisAtASpeed":
        return self._Cast_SpringDamperConnectionModalAnalysisAtASpeed(self)
