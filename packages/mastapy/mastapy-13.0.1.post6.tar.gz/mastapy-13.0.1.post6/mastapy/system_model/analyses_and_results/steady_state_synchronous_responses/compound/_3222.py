"""StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3133,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3092,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3121,
        _3149,
        _3175,
        _3181,
        _3151,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse"
)


class StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse(
    _3133.BevelGearMeshCompoundSteadyStateSynchronousResponse
):
    """StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3133.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3133.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3121.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3121,
            )

            return self._parent._cast(
                _3121.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3175.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3092.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3092.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse(
                self
            )
        )
