"""TorqueConverterConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "TorqueConverterConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344, _6312
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionDynamicAnalysis")


class TorqueConverterConnectionDynamicAnalysis(_6314.CouplingConnectionDynamicAnalysis):
    """TorqueConverterConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionDynamicAnalysis"
    )

    class _Cast_TorqueConverterConnectionDynamicAnalysis:
        """Special nested class for casting TorqueConverterConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
            parent: "TorqueConverterConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_dynamic_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_6314.CouplingConnectionDynamicAnalysis":
            return self._parent._cast(_6314.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_6344.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_6312.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
        ) -> "TorqueConverterConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
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
    def connection_load_case(self: Self) -> "_6973.TorqueConverterConnectionLoadCase":
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
    ) -> "TorqueConverterConnectionDynamicAnalysis._Cast_TorqueConverterConnectionDynamicAnalysis":
        return self._Cast_TorqueConverterConnectionDynamicAnalysis(self)
