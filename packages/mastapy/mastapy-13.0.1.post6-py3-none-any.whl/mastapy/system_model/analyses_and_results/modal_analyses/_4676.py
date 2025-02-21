"""RollingRingModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RollingRingModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.system_deflections import _2799
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingModalAnalysis",)


Self = TypeVar("Self", bound="RollingRingModalAnalysis")


class RollingRingModalAnalysis(_4611.CouplingHalfModalAnalysis):
    """RollingRingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingModalAnalysis")

    class _Cast_RollingRingModalAnalysis:
        """Special nested class for casting RollingRingModalAnalysis to subclasses."""

        def __init__(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
            parent: "RollingRingModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4611.CouplingHalfModalAnalysis":
            return self._parent._cast(_4611.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "RollingRingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2596.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2799.RollingRingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis":
        return self._Cast_RollingRingModalAnalysis(self)
