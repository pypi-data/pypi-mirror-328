"""HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.system_deflections import _2784
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7065,
        _7091,
        _7098,
        _7067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation")


class HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7036.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7036.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7036.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7065.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6928.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2784.HypoidGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection

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
    ) -> "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
