"""CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293
    from mastapy.system_model.analyses_and_results.system_deflections import _2753
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7098,
        _7067,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7041.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7041.BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7041.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7067.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2753.CVTBeltConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection

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
    ) -> "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
