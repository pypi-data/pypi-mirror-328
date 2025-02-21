"""SpringDamperConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpringDamperConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.static_loads import _6978
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3851,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionStabilityAnalysis")


class SpringDamperConnectionStabilityAnalysis(
    _3821.CouplingConnectionStabilityAnalysis
):
    """SpringDamperConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionStabilityAnalysis"
    )

    class _Cast_SpringDamperConnectionStabilityAnalysis:
        """Special nested class for casting SpringDamperConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
            parent: "SpringDamperConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_stability_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_3821.CouplingConnectionStabilityAnalysis":
            return self._parent._cast(_3821.CouplingConnectionStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
        ) -> "SpringDamperConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2370.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6978.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionStabilityAnalysis._Cast_SpringDamperConnectionStabilityAnalysis":
        return self._Cast_SpringDamperConnectionStabilityAnalysis(self)
