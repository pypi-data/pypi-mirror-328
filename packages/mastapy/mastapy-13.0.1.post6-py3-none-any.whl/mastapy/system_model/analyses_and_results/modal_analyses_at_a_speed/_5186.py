"""KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5149,
        _5175,
        _5182,
        _5152,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed(
    _5183.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_5183.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_5149.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_5175.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_5182.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_5152.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6917.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed(
            self
        )
