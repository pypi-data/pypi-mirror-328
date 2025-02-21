"""PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7109,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.system_deflections import _2789
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7009,
        _7046,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7109.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7109.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7109.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7009.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7009,
            )

            return self._parent._cast(
                _7009.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6933.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "_2789.PlanetaryConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection

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
    ) -> "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
