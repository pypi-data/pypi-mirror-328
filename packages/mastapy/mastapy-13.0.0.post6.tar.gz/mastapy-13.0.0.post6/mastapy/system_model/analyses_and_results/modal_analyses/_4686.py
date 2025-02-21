"""SpringDamperHalfModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpringDamperHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2811
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4657,
        _4596,
        _4661,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfModalAnalysis")


class SpringDamperHalfModalAnalysis(_4610.CouplingHalfModalAnalysis):
    """SpringDamperHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfModalAnalysis")

    class _Cast_SpringDamperHalfModalAnalysis:
        """Special nested class for casting SpringDamperHalfModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
            parent: "SpringDamperHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_4610.CouplingHalfModalAnalysis":
            return self._parent._cast(_4610.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_4657.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_4596.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_4661.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "SpringDamperHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2811.SpringDamperHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis":
        return self._Cast_SpringDamperHalfModalAnalysis(self)
