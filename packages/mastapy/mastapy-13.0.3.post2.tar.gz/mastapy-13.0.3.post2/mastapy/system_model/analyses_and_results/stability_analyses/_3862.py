"""MeasurementComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "MeasurementComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentStabilityAnalysis")


class MeasurementComponentStabilityAnalysis(_3911.VirtualComponentStabilityAnalysis):
    """MeasurementComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentStabilityAnalysis"
    )

    class _Cast_MeasurementComponentStabilityAnalysis:
        """Special nested class for casting MeasurementComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
            parent: "MeasurementComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_stability_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_3911.VirtualComponentStabilityAnalysis":
            return self._parent._cast(_3911.VirtualComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
        ) -> "MeasurementComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2483.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6944.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentStabilityAnalysis._Cast_MeasurementComponentStabilityAnalysis":
        return self._Cast_MeasurementComponentStabilityAnalysis(self)
