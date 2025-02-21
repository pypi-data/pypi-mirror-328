"""SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7028,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7015,
        _7044,
        _7070,
        _7077,
        _7046,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
)


class SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7028.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7028.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7028.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7015.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7015,
            )

            return self._parent._cast(
                _7015.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7044.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7070.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6955.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2807.SpiralBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
            self
        )
