"""PartToPartShearCouplingHalfStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartToPartShearCouplingHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3842,
        _3788,
        _3844,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfStabilityAnalysis")


class PartToPartShearCouplingHalfStabilityAnalysis(_3801.CouplingHalfStabilityAnalysis):
    """PartToPartShearCouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
            parent: "PartToPartShearCouplingHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3801.CouplingHalfStabilityAnalysis":
            return self._parent._cast(_3801.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3842.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3788.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3844.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "PartToPartShearCouplingHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
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
        self: Self,
        instance_to_wrap: "PartToPartShearCouplingHalfStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6931.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingHalfStabilityAnalysis(self)
