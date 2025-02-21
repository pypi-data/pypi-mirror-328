"""BeltDriveSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3082,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BeltDriveSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3025,
        _2983,
        _3063,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BeltDriveSteadyStateSynchronousResponse")


class BeltDriveSteadyStateSynchronousResponse(
    _3082.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """BeltDriveSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveSteadyStateSynchronousResponse"
    )

    class _Cast_BeltDriveSteadyStateSynchronousResponse:
        """Special nested class for casting BeltDriveSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
            parent: "BeltDriveSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_3082.SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_2983.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_3063.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "_3025.CVTSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.CVTSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "BeltDriveSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "BeltDriveSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
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
    def assembly_load_case(self: Self) -> "_6822.BeltDriveLoadCase":
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
    ) -> "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse":
        return self._Cast_BeltDriveSteadyStateSynchronousResponse(self)
