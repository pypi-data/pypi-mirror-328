"""PointLoadModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PointLoadModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.system_deflections import _2791
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadModalAnalysis",)


Self = TypeVar("Self", bound="PointLoadModalAnalysis")


class PointLoadModalAnalysis(_4706.VirtualComponentModalAnalysis):
    """PointLoadModalAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadModalAnalysis")

    class _Cast_PointLoadModalAnalysis:
        """Special nested class for casting PointLoadModalAnalysis to subclasses."""

        def __init__(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
            parent: "PointLoadModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_4706.VirtualComponentModalAnalysis":
            return self._parent._cast(_4706.VirtualComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis",
        ) -> "PointLoadModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2791.PointLoadSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PointLoadModalAnalysis._Cast_PointLoadModalAnalysis":
        return self._Cast_PointLoadModalAnalysis(self)
