"""CoaxialConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CoaxialConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.static_loads import _6837
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6321,
        _6280,
        _6312,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionDynamicAnalysis")


class CoaxialConnectionDynamicAnalysis(
    _6376.ShaftToMountableComponentConnectionDynamicAnalysis
):
    """CoaxialConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionDynamicAnalysis")

    class _Cast_CoaxialConnectionDynamicAnalysis:
        """Special nested class for casting CoaxialConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
            parent: "CoaxialConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6376.ShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6376.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(
                _6280.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6312.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(
                _6321.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def coaxial_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "CoaxialConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnectionDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6837.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis":
        return self._Cast_CoaxialConnectionDynamicAnalysis(self)
