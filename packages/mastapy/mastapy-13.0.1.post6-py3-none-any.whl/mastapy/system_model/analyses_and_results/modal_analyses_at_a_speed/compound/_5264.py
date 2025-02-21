"""BevelGearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5252,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5133,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5259,
        _5347,
        _5353,
        _5356,
        _5374,
        _5280,
        _5306,
        _5312,
        _5282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundModalAnalysisAtASpeed")


class BevelGearMeshCompoundModalAnalysisAtASpeed(
    _5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """BevelGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_BevelGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting BevelGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
            parent: "BevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5306.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5282.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5259.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5347.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5353.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5356.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5374.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "BevelGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5133.BevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelGearMeshModalAnalysisAtASpeed]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5133.BevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelGearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundModalAnalysisAtASpeed._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_BevelGearMeshCompoundModalAnalysisAtASpeed(self)
