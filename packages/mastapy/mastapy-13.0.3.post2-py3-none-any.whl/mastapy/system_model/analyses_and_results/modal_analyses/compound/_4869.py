"""TorqueConverterTurbineCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "TorqueConverterTurbineCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.modal_analyses import _4725
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4826,
        _4774,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundModalAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundModalAnalysis")


class TorqueConverterTurbineCompoundModalAnalysis(
    _4788.CouplingHalfCompoundModalAnalysis
):
    """TorqueConverterTurbineCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundModalAnalysis"
    )

    class _Cast_TorqueConverterTurbineCompoundModalAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
            parent: "TorqueConverterTurbineCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_4788.CouplingHalfCompoundModalAnalysis":
            return self._parent._cast(_4788.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_4826.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
        ) -> "TorqueConverterTurbineCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4725.TorqueConverterTurbineModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4725.TorqueConverterTurbineModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineCompoundModalAnalysis._Cast_TorqueConverterTurbineCompoundModalAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundModalAnalysis(self)
