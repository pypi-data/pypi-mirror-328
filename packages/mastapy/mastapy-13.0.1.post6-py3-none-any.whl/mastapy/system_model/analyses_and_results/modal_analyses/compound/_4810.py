"""PartToPartShearCouplingHalfCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.modal_analyses import _4664
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4805,
        _4753,
        _4807,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCompoundModalAnalysis")


class PartToPartShearCouplingHalfCompoundModalAnalysis(
    _4767.CouplingHalfCompoundModalAnalysis
):
    """PartToPartShearCouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfCompoundModalAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfCompoundModalAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
            parent: "PartToPartShearCouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_4767.CouplingHalfCompoundModalAnalysis":
            return self._parent._cast(_4767.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_4805.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
        ) -> "PartToPartShearCouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_4664.PartToPartShearCouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis]

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
    ) -> "List[_4664.PartToPartShearCouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis]

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
    ) -> "PartToPartShearCouplingHalfCompoundModalAnalysis._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis":
        return self._Cast_PartToPartShearCouplingHalfCompoundModalAnalysis(self)
