"""BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3517,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3522,
        _3510,
        _3538,
        _3564,
        _3581,
        _3529,
        _3583,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"
)


class BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed(
    _3517.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3517.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3517.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3522.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3510.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(_3564.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3581.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
