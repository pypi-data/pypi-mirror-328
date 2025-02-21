"""RingPinsModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "RingPinsModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2590
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.modal_analyses import _4618, _4683
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsModalAnalysis",)


Self = TypeVar("Self", bound="RingPinsModalAnalysis")


class RingPinsModalAnalysis(_4679.MountableComponentModalAnalysis):
    """RingPinsModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsModalAnalysis")

    class _Cast_RingPinsModalAnalysis:
        """Special nested class for casting RingPinsModalAnalysis to subclasses."""

        def __init__(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
            parent: "RingPinsModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "RingPinsModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2815.RingPinsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis":
        return self._Cast_RingPinsModalAnalysis(self)
