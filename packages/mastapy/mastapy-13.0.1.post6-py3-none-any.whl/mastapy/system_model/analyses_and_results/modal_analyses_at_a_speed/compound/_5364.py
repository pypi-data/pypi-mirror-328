"""TorqueConverterCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5284,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5236,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5345,
        _5247,
        _5326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterCompoundModalAnalysisAtASpeed")


class TorqueConverterCompoundModalAnalysisAtASpeed(
    _5284.CouplingCompoundModalAnalysisAtASpeed
):
    """TorqueConverterCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundModalAnalysisAtASpeed"
    )

    class _Cast_TorqueConverterCompoundModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
            parent: "TorqueConverterCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_5284.CouplingCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5284.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_5247.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_5326.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
        ) -> "TorqueConverterCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "TorqueConverterCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2607.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5236.TorqueConverterModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5236.TorqueConverterModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterCompoundModalAnalysisAtASpeed._Cast_TorqueConverterCompoundModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterCompoundModalAnalysisAtASpeed(self)
