"""FlexiblePinAssemblyModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4957,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "FlexiblePinAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.static_loads import _6889
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4857,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyModalAnalysisAtAStiffness")


class FlexiblePinAssemblyModalAnalysisAtAStiffness(
    _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """FlexiblePinAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting FlexiblePinAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
            parent: "FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4957.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4857.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
        ) -> "FlexiblePinAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness",
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
        instance_to_wrap: "FlexiblePinAssemblyModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2454.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6889.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyModalAnalysisAtAStiffness._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness":
        return self._Cast_FlexiblePinAssemblyModalAnalysisAtAStiffness(self)
