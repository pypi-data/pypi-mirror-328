"""PartToPartShearCouplingHalfCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4482,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4395
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4520,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCompoundParametricStudyTool")


class PartToPartShearCouplingHalfCompoundParametricStudyTool(
    _4482.CouplingHalfCompoundParametricStudyTool
):
    """PartToPartShearCouplingHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
            parent: "PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_4482.CouplingHalfCompoundParametricStudyTool":
            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_4520.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
        ) -> "PartToPartShearCouplingHalfCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundParametricStudyTool.TYPE",
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
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6931.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4395.PartToPartShearCouplingHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingHalfParametricStudyTool]

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
    ) -> "List[_4395.PartToPartShearCouplingHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingHalfParametricStudyTool]

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
    ) -> "PartToPartShearCouplingHalfCompoundParametricStudyTool._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool":
        return self._Cast_PartToPartShearCouplingHalfCompoundParametricStudyTool(self)
