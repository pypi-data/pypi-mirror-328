"""BevelGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6823,
        _6954,
        _6960,
        _6963,
        _6986,
        _6846,
        _6892,
        _6911,
        _6849,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshLoadCase",)


Self = TypeVar("Self", bound="BevelGearMeshLoadCase")


class BevelGearMeshLoadCase(_6814.AGMAGleasonConicalGearMeshLoadCase):
    """BevelGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshLoadCase")

    class _Cast_BevelGearMeshLoadCase:
        """Special nested class for casting BevelGearMeshLoadCase to subclasses."""

        def __init__(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
            parent: "BevelGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6814.AGMAGleasonConicalGearMeshLoadCase":
            return self._parent._cast(_6814.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6846.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6892.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6911.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6849.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6823.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialGearMeshLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6954.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6960.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6963.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "_6986.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.ZerolBevelGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase",
        ) -> "BevelGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshLoadCase.TYPE"):
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
    def cast_to(self: Self) -> "BevelGearMeshLoadCase._Cast_BevelGearMeshLoadCase":
        return self._Cast_BevelGearMeshLoadCase(self)
