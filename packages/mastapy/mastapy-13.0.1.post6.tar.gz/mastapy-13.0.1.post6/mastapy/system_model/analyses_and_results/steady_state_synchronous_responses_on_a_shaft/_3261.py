"""BevelGearMeshSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3249,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3256,
        _3344,
        _3351,
        _3354,
        _3372,
        _3277,
        _3303,
        _3310,
        _3280,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="BevelGearMeshSteadyStateSynchronousResponseOnAShaft")


class BevelGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """BevelGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3277.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3303.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3256.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3344.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3351.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3354.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3372.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2303.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelGearMeshSteadyStateSynchronousResponseOnAShaft(self)
