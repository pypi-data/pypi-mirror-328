"""ConceptGearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5145,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5311,
        _5281,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptGearMeshCompoundModalAnalysisAtASpeed")


class ConceptGearMeshCompoundModalAnalysisAtASpeed(
    _5305.GearMeshCompoundModalAnalysisAtASpeed
):
    """ConceptGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConceptGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
            parent: "ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5305.GearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5305.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5311.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5281.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "ConceptGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ConceptGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2305.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2305.ConceptGearMesh":
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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5145.ConceptGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptGearMeshModalAnalysisAtASpeed]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5145.ConceptGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptGearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshCompoundModalAnalysisAtASpeed._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_ConceptGearMeshCompoundModalAnalysisAtASpeed(self)
