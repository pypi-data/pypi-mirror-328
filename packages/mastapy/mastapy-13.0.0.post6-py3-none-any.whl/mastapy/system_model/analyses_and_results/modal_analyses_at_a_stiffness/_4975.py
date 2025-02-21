"""TorqueConverterConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4893,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "TorqueConverterConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4922,
        _4891,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="TorqueConverterConnectionModalAnalysisAtAStiffness")


class TorqueConverterConnectionModalAnalysisAtAStiffness(
    _4893.CouplingConnectionModalAnalysisAtAStiffness
):
    """TorqueConverterConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_TorqueConverterConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
            parent: "TorqueConverterConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_4893.CouplingConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4893.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_4922.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_4891.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
        ) -> "TorqueConverterConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6972.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionModalAnalysisAtAStiffness._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterConnectionModalAnalysisAtAStiffness(self)
