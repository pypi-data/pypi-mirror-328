"""CouplingHalfCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4610
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4750,
        _4755,
        _4769,
        _4809,
        _4815,
        _4819,
        _4831,
        _4841,
        _4842,
        _4843,
        _4846,
        _4847,
        _4752,
        _4806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysis")


class CouplingHalfCompoundModalAnalysis(_4804.MountableComponentCompoundModalAnalysis):
    """CouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysis")

    class _Cast_CouplingHalfCompoundModalAnalysis:
        """Special nested class for casting CouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
            parent: "CouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4804.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4752.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4806.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4750.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4755.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4769.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CVTPulleyCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4809.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(
                _4809.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4815.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PulleyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4819.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RollingRingCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4831.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.SpringDamperHalfCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4841.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4842.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4843.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4846.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "_4847.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "CouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4610.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4610.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis":
        return self._Cast_CouplingHalfCompoundModalAnalysis(self)
