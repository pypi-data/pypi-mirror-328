"""CouplingHalfModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4936,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CouplingHalfModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4879,
        _4884,
        _4899,
        _4940,
        _4947,
        _4952,
        _4962,
        _4972,
        _4974,
        _4975,
        _4978,
        _4979,
        _4882,
        _4938,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingHalfModalAnalysisAtAStiffness")


class CouplingHalfModalAnalysisAtAStiffness(
    _4936.MountableComponentModalAnalysisAtAStiffness
):
    """CouplingHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingHalfModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingHalfModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
            parent: "CouplingHalfModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4936.MountableComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4882.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4938.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4879.ClutchHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4884.ConceptCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(
                _4884.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4899.CVTPulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4940.PartToPartShearCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(
                _4940.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4947.PulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(_4947.PulleyModalAnalysisAtAStiffness)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4952.RollingRingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(_4952.RollingRingModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4962.SpringDamperHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(_4962.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4972.SynchroniserHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4972,
            )

            return self._parent._cast(_4972.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4974.SynchroniserPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(_4974.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4975.SynchroniserSleeveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(_4975.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4978.TorqueConverterPumpModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "_4979.TorqueConverterTurbineModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(
                _4979.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
        ) -> "CouplingHalfModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingHalfModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfModalAnalysisAtAStiffness._Cast_CouplingHalfModalAnalysisAtAStiffness":
        return self._Cast_CouplingHalfModalAnalysisAtAStiffness(self)
