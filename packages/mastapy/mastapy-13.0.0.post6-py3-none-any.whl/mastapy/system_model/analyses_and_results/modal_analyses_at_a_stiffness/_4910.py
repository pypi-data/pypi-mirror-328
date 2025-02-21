"""FaceGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4915,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "FaceGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4922,
        _4891,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FaceGearMeshModalAnalysisAtAStiffness")


class FaceGearMeshModalAnalysisAtAStiffness(_4915.GearMeshModalAnalysisAtAStiffness):
    """FaceGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_FaceGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting FaceGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
            parent: "FaceGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_4915.GearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(_4915.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_4922.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_4891.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
        ) -> "FaceGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "FaceGearMeshModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2311.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6885.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshModalAnalysisAtAStiffness._Cast_FaceGearMeshModalAnalysisAtAStiffness":
        return self._Cast_FaceGearMeshModalAnalysisAtAStiffness(self)
