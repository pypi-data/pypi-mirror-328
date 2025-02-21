"""CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7091,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.system_model.analyses_and_results.system_deflections import _2760
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7098,
        _7067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"
)


class CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7091.GearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7091.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6885.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

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
    ) -> "_2760.CylindricalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation(
            self
        )
