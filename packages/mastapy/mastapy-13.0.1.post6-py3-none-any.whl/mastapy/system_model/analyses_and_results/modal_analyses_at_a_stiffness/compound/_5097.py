"""StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5005,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4967,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4993,
        _5021,
        _5047,
        _5053,
        _5023,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundModalAnalysisAtAStiffness")


class StraightBevelGearMeshCompoundModalAnalysisAtAStiffness(
    _5005.BevelGearMeshCompoundModalAnalysisAtAStiffness
):
    """StraightBevelGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5005.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_4993.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4993,
            )

            return self._parent._cast(
                _4993.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2327.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2327.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

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
    ) -> "List[_4967.StraightBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearMeshModalAnalysisAtAStiffness]

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
    ) -> "List[_4967.StraightBevelGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelGearMeshModalAnalysisAtAStiffness]

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
    ) -> "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelGearMeshCompoundModalAnalysisAtAStiffness(self)
