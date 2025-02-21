"""MultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "MultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5460
    from mastapy.nodal_analysis.system_solvers import _118
    from mastapy.system_model.analyses_and_results.analysis_cases import _7534
    from mastapy.system_model.analyses_and_results import _2650


__docformat__ = "restructuredtext en"
__all__ = ("MultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MultibodyDynamicsAnalysis")


class MultibodyDynamicsAnalysis(_7550.TimeSeriesLoadAnalysisCase):
    """MultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultibodyDynamicsAnalysis")

    class _Cast_MultibodyDynamicsAnalysis:
        """Special nested class for casting MultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis",
            parent: "MultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def time_series_load_analysis_case(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis",
        ) -> "_7550.TimeSeriesLoadAnalysisCase":
            return self._parent._cast(_7550.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis",
        ) -> "_7534.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.AnalysisCase)

        @property
        def context(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis",
        ) -> "_2650.Context":
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def multibody_dynamics_analysis(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis",
        ) -> "MultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_interface_analysis_results_available(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasInterfaceAnalysisResultsAvailable

        if temp is None:
            return False

        return temp

    @property
    def percentage_time_spent_in_masta_solver(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageTimeSpentInMASTASolver

        if temp is None:
            return 0.0

        return temp

    @property
    def mbd_options(self: Self) -> "_5460.MBDAnalysisOptions":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MBDAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MBDOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transient_solver(self: Self) -> "_118.TransientSolver":
        """mastapy.nodal_analysis.system_solvers.TransientSolver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransientSolver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MultibodyDynamicsAnalysis._Cast_MultibodyDynamicsAnalysis":
        return self._Cast_MultibodyDynamicsAnalysis(self)
