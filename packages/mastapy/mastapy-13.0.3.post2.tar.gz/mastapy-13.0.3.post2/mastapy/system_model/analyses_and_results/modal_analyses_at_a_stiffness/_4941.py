"""HypoidGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4882,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "HypoidGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4910,
        _4937,
        _4944,
        _4913,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="HypoidGearMeshModalAnalysisAtAStiffness")


class HypoidGearMeshModalAnalysisAtAStiffness(
    _4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
):
    """HypoidGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_HypoidGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting HypoidGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
            parent: "HypoidGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4882.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4910.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4937.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4944.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(
                _4944.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_4913.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
        ) -> "HypoidGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "HypoidGearMeshModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6928.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshModalAnalysisAtAStiffness._Cast_HypoidGearMeshModalAnalysisAtAStiffness":
        return self._Cast_HypoidGearMeshModalAnalysisAtAStiffness(self)
