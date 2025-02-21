"""BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3154,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3015,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3142,
        _3170,
        _3196,
        _3202,
        _3172,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse"
)


class BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse(
    _3154.BevelGearMeshCompoundSteadyStateSynchronousResponse
):
    """BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3154.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3142.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3196.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "List[_3015.BevelDifferentialGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearMeshSteadyStateSynchronousResponse]

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
    ) -> "List[_3015.BevelDifferentialGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearMeshSteadyStateSynchronousResponse]

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
    ) -> "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse(
                self
            )
        )
