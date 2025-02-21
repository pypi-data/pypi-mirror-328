"""CVTBeltConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTBeltConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5449, _5414
    from mastapy.system_model.analyses_and_results.analysis_cases import _7542, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionMultibodyDynamicsAnalysis")


class CVTBeltConnectionMultibodyDynamicsAnalysis(
    _5387.BeltConnectionMultibodyDynamicsAnalysis
):
    """CVTBeltConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_CVTBeltConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTBeltConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
            parent: "CVTBeltConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_5387.BeltConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5387.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_5414.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_7542.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
        ) -> "CVTBeltConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2273.CVTBeltConnection":
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
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis":
        return self._Cast_CVTBeltConnectionMultibodyDynamicsAnalysis(self)
