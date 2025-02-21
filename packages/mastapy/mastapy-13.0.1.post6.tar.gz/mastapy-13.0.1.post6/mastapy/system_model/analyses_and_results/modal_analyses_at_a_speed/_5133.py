"""BevelGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5128,
        _5217,
        _5223,
        _5226,
        _5244,
        _5149,
        _5175,
        _5182,
        _5152,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtASpeed")


class BevelGearMeshModalAnalysisAtASpeed(
    _5121.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
):
    """BevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtASpeed")

    class _Cast_BevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting BevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
            parent: "BevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5121.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(
                _5121.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5149.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5175.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5182.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5152.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5128.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5217.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5223.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(
                _5223.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5226.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "_5244.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "BevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2303.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed":
        return self._Cast_BevelGearMeshModalAnalysisAtASpeed(self)
