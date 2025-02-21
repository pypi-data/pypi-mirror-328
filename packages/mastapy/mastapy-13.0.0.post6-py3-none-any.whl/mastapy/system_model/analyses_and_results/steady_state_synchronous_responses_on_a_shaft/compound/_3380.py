"""AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3408,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3249,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3387,
        _3392,
        _3438,
        _3475,
        _3481,
        _3484,
        _3502,
        _3434,
        _3440,
        _3410,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3408.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3408.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3434.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3440.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3387.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3392.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3392,
            )

            return self._parent._cast(
                _3392.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3438.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3481.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3484.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3249.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
