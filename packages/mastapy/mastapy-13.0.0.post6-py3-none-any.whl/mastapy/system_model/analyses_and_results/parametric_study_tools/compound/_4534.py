"""RollingRingCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4481,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "RollingRingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4519,
        _4467,
        _4521,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="RollingRingCompoundParametricStudyTool")


class RollingRingCompoundParametricStudyTool(
    _4481.CouplingHalfCompoundParametricStudyTool
):
    """RollingRingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingCompoundParametricStudyTool"
    )

    class _Cast_RollingRingCompoundParametricStudyTool:
        """Special nested class for casting RollingRingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
            parent: "RollingRingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_4481.CouplingHalfCompoundParametricStudyTool":
            return self._parent._cast(_4481.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_4519.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_4467.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_4521.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
        ) -> "RollingRingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "RollingRingCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2596.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6947.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

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
    ) -> "List[_4406.RollingRingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingParametricStudyTool]

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
    def planetaries(self: Self) -> "List[RollingRingCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.RollingRingCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4406.RollingRingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RollingRingParametricStudyTool]

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
    ) -> "RollingRingCompoundParametricStudyTool._Cast_RollingRingCompoundParametricStudyTool":
        return self._Cast_RollingRingCompoundParametricStudyTool(self)
