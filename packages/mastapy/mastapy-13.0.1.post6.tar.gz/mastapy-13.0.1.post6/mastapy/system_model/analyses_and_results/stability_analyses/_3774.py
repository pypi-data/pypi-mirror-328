"""BevelDifferentialGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.static_loads import _6824
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3767,
        _3795,
        _3823,
        _3830,
        _3798,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshStabilityAnalysis")


class BevelDifferentialGearMeshStabilityAnalysis(_3779.BevelGearMeshStabilityAnalysis):
    """BevelDifferentialGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshStabilityAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshStabilityAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
            parent: "BevelDifferentialGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3779.BevelGearMeshStabilityAnalysis":
            return self._parent._cast(_3779.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3767.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3795.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3823.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3830.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_3798.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
        ) -> "BevelDifferentialGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6824.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "BevelDifferentialGearMeshStabilityAnalysis._Cast_BevelDifferentialGearMeshStabilityAnalysis":
        return self._Cast_BevelDifferentialGearMeshStabilityAnalysis(self)
