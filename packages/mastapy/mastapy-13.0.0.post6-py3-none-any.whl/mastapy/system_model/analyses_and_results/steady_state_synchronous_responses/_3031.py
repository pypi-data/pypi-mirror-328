"""CylindricalGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3043,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CylindricalGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6865
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3032,
        _3030,
        _3068,
        _3082,
        _2983,
        _3063,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CylindricalGearSetSteadyStateSynchronousResponse")


class CylindricalGearSetSteadyStateSynchronousResponse(
    _3043.GearSetSteadyStateSynchronousResponse
):
    """CylindricalGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_CylindricalGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
            parent: "CylindricalGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_3043.GearSetSteadyStateSynchronousResponse":
            return self._parent._cast(_3043.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_3082.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_2983.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_3063.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "_3068.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(
                _3068.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
        ) -> "CylindricalGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6865.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3032.CylindricalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3030.CylindricalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetSteadyStateSynchronousResponse._Cast_CylindricalGearSetSteadyStateSynchronousResponse":
        return self._Cast_CylindricalGearSetSteadyStateSynchronousResponse(self)
