"""FaceGearMeshSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3562,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3569,
        _3539,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="FaceGearMeshSteadyStateSynchronousResponseAtASpeed")


class FaceGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3562.GearMeshSteadyStateSynchronousResponseAtASpeed
):
    """FaceGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting FaceGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.GearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3562.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3569.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2311.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6885.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed(self)
