"""BevelGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4860,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4867,
        _4957,
        _4963,
        _4966,
        _4984,
        _4888,
        _4915,
        _4922,
        _4891,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtAStiffness")


class BevelGearMeshModalAnalysisAtAStiffness(
    _4860.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
):
    """BevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
            parent: "BevelGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4860.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4860.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4888.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4915.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4922.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4891.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4867.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4867,
            )

            return self._parent._cast(
                _4867.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4957.SpiralBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4963.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4966.StraightBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "_4984.ZerolBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "BevelGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtAStiffness.TYPE"
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
    ) -> "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness":
        return self._Cast_BevelGearMeshModalAnalysisAtAStiffness(self)
