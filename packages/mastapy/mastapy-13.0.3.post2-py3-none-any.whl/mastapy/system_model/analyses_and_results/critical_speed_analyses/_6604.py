"""CriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7571
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("CriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CriticalSpeedAnalysis")


class CriticalSpeedAnalysis(_7571.StaticLoadAnalysisCase):
    """CriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CriticalSpeedAnalysis")

    class _Cast_CriticalSpeedAnalysis:
        """Special nested class for casting CriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
            parent: "CriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "_7571.StaticLoadAnalysisCase":
            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def critical_speed_analysis(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "CriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_speed_analysis_options(
        self: Self,
    ) -> "_6606.CriticalSpeedAnalysisOptions":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis":
        return self._Cast_CriticalSpeedAnalysis(self)
