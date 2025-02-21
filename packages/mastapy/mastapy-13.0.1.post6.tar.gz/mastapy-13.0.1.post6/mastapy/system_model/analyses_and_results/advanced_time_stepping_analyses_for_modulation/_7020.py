"""BeltConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7077,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.system_model.analyses_and_results.system_deflections import _2699
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7052,
        _7046,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BeltConnectionAdvancedTimeSteppingAnalysisForModulation")


class BeltConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """BeltConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BeltConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7077.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BeltConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6821.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2699.BeltConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection

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
    ) -> "BeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BeltConnectionAdvancedTimeSteppingAnalysisForModulation(self)
