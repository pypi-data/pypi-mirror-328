"""WormGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "WormGearModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2838
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearModalAnalysis",)


Self = TypeVar("Self", bound="WormGearModalAnalysis")


class WormGearModalAnalysis(_4636.GearModalAnalysis):
    """WormGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearModalAnalysis")

    class _Cast_WormGearModalAnalysis:
        """Special nested class for casting WormGearModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
            parent: "WormGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_4636.GearModalAnalysis":
            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis",
        ) -> "WormGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearModalAnalysis._Cast_WormGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2838.WormGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearModalAnalysis._Cast_WormGearModalAnalysis":
        return self._Cast_WormGearModalAnalysis(self)
