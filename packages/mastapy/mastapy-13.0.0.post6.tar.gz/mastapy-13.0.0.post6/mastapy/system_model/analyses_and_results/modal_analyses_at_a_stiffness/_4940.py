"""PartToPartShearCouplingModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4895,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PartToPartShearCouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4956,
        _4856,
        _4937,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PartToPartShearCouplingModalAnalysisAtAStiffness")


class PartToPartShearCouplingModalAnalysisAtAStiffness(
    _4895.CouplingModalAnalysisAtAStiffness
):
    """PartToPartShearCouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingModalAnalysisAtAStiffness"
    )

    class _Cast_PartToPartShearCouplingModalAnalysisAtAStiffness:
        """Special nested class for casting PartToPartShearCouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
            parent: "PartToPartShearCouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4895.CouplingModalAnalysisAtAStiffness":
            return self._parent._cast(_4895.CouplingModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4956.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(
                _4956.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4856.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4856,
            )

            return self._parent._cast(_4856.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_4937.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
        ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PartToPartShearCouplingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6931.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness":
        return self._Cast_PartToPartShearCouplingModalAnalysisAtAStiffness(self)
