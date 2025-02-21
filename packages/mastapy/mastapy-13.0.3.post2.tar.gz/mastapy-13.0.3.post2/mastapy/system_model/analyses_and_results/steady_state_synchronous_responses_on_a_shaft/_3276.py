"""BeltDriveSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3364,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BeltDriveSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3308,
        _3266,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="BeltDriveSteadyStateSynchronousResponseOnAShaft")


class BeltDriveSteadyStateSynchronousResponseOnAShaft(
    _3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
):
    """BeltDriveSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BeltDriveSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
            parent: "BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3308.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(_3308.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
        ) -> "BeltDriveSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BeltDriveSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveSteadyStateSynchronousResponseOnAShaft._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BeltDriveSteadyStateSynchronousResponseOnAShaft(self)
