"""WormGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4938,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "WormGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7004
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="WormGearModalAnalysisAtAStiffness")


class WormGearModalAnalysisAtAStiffness(_4938.GearModalAnalysisAtAStiffness):
    """WormGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearModalAnalysisAtAStiffness")

    class _Cast_WormGearModalAnalysisAtAStiffness:
        """Special nested class for casting WormGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
            parent: "WormGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_4938.GearModalAnalysisAtAStiffness":
            return self._parent._cast(_4938.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
        ) -> "WormGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "WormGearModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.WormGear":
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
    def component_load_case(self: Self) -> "_7004.WormGearLoadCase":
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
    def cast_to(
        self: Self,
    ) -> "WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness":
        return self._Cast_WormGearModalAnalysisAtAStiffness(self)
