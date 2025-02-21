"""VirtualComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "VirtualComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3840,
        _3841,
        _3851,
        _3852,
        _3889,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentStabilityAnalysis")


class VirtualComponentStabilityAnalysis(_3842.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentStabilityAnalysis")

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
            parent: "VirtualComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3840.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3841.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3851.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3852.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3889.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "VirtualComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis":
        return self._Cast_VirtualComponentStabilityAnalysis(self)
