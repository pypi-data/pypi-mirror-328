"""FlexiblePinAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6268
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
        _6274,
        _6270,
        _6271,
        _6272,
        _6273,
        _6275,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAnalysis")


class FlexiblePinAnalysis(_6268.CombinationAnalysis):
    """FlexiblePinAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysis")

    class _Cast_FlexiblePinAnalysis:
        """Special nested class for casting FlexiblePinAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
            parent: "FlexiblePinAnalysis",
        ):
            self._parent = parent

        @property
        def combination_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6268.CombinationAnalysis":
            return self._parent._cast(_6268.CombinationAnalysis)

        @property
        def flexible_pin_analysis_concept_level(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6270.FlexiblePinAnalysisConceptLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6270,
            )

            return self._parent._cast(_6270.FlexiblePinAnalysisConceptLevel)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6271.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6271,
            )

            return self._parent._cast(
                _6271.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
            )

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6272.FlexiblePinAnalysisGearAndBearingRating":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6272,
            )

            return self._parent._cast(_6272.FlexiblePinAnalysisGearAndBearingRating)

        @property
        def flexible_pin_analysis_manufacture_level(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6273.FlexiblePinAnalysisManufactureLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6273,
            )

            return self._parent._cast(_6273.FlexiblePinAnalysisManufactureLevel)

        @property
        def flexible_pin_analysis_stop_start_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "_6275.FlexiblePinAnalysisStopStartAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6275,
            )

            return self._parent._cast(_6275.FlexiblePinAnalysisStopStartAnalysis)

        @property
        def flexible_pin_analysis(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis",
        ) -> "FlexiblePinAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_options(self: Self) -> "_6274.FlexiblePinAnalysisOptions":
        """mastapy.system_model.analyses_and_results.flexible_pin_analyses.FlexiblePinAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FlexiblePinAnalysis._Cast_FlexiblePinAnalysis":
        return self._Cast_FlexiblePinAnalysis(self)
