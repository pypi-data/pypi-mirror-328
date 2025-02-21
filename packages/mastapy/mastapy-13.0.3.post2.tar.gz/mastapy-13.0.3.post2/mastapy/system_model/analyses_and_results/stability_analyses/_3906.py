"""TorqueConverterConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "TorqueConverterConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2372
    from mastapy.system_model.analyses_and_results.static_loads import _6994
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3851,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionStabilityAnalysis")


class TorqueConverterConnectionStabilityAnalysis(
    _3821.CouplingConnectionStabilityAnalysis
):
    """TorqueConverterConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionStabilityAnalysis"
    )

    class _Cast_TorqueConverterConnectionStabilityAnalysis:
        """Special nested class for casting TorqueConverterConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
            parent: "TorqueConverterConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_stability_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_3821.CouplingConnectionStabilityAnalysis":
            return self._parent._cast(_3821.CouplingConnectionStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
        ) -> "TorqueConverterConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2372.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6994.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionStabilityAnalysis._Cast_TorqueConverterConnectionStabilityAnalysis":
        return self._Cast_TorqueConverterConnectionStabilityAnalysis(self)
