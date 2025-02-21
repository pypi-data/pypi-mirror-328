"""ConceptGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4937,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConceptGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6864
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4944,
        _4913,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConceptGearMeshModalAnalysisAtAStiffness")


class ConceptGearMeshModalAnalysisAtAStiffness(_4937.GearMeshModalAnalysisAtAStiffness):
    """ConceptGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_ConceptGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
            parent: "ConceptGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_4937.GearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(_4937.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_4944.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(
                _4944.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_4913.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
        ) -> "ConceptGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConceptGearMeshModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.ConceptGearMesh":
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
    def connection_load_case(self: Self) -> "_6864.ConceptGearMeshLoadCase":
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
    ) -> "ConceptGearMeshModalAnalysisAtAStiffness._Cast_ConceptGearMeshModalAnalysisAtAStiffness":
        return self._Cast_ConceptGearMeshModalAnalysisAtAStiffness(self)
