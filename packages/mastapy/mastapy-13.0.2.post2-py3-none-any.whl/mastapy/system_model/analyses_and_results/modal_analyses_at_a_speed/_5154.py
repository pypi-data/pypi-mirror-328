"""ConceptGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5190,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptGearMeshModalAnalysisAtASpeed")


class ConceptGearMeshModalAnalysisAtASpeed(_5183.GearMeshModalAnalysisAtASpeed):
    """ConceptGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearMeshModalAnalysisAtASpeed")

    class _Cast_ConceptGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting ConceptGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
            parent: "ConceptGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_5183.GearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5183.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_5190.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(
                _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
        ) -> "ConceptGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ConceptGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2312.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6851.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

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
    ) -> "ConceptGearMeshModalAnalysisAtASpeed._Cast_ConceptGearMeshModalAnalysisAtASpeed":
        return self._Cast_ConceptGearMeshModalAnalysisAtASpeed(self)
