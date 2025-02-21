"""CVTBeltConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4874,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTBeltConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2280
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4931,
        _4900,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTBeltConnectionModalAnalysisAtAStiffness")


class CVTBeltConnectionModalAnalysisAtAStiffness(
    _4874.BeltConnectionModalAnalysisAtAStiffness
):
    """CVTBeltConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_CVTBeltConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CVTBeltConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
            parent: "CVTBeltConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4874.BeltConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4874.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4931.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(
                _4931.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_4900.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
        ) -> "CVTBeltConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2280.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionModalAnalysisAtAStiffness._Cast_CVTBeltConnectionModalAnalysisAtAStiffness":
        return self._Cast_CVTBeltConnectionModalAnalysisAtAStiffness(self)
