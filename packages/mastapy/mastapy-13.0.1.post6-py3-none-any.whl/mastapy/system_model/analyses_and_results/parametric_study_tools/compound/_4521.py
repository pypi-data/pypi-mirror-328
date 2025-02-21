"""OilSealCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "OilSealCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4520,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="OilSealCompoundParametricStudyTool")


class OilSealCompoundParametricStudyTool(_4479.ConnectorCompoundParametricStudyTool):
    """OilSealCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundParametricStudyTool")

    class _Cast_OilSealCompoundParametricStudyTool:
        """Special nested class for casting OilSealCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
            parent: "OilSealCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connector_compound_parametric_study_tool(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_4479.ConnectorCompoundParametricStudyTool":
            return self._parent._cast(_4479.ConnectorCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_4520.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
        ) -> "OilSealCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "OilSealCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(self: Self) -> "_6927.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "List[_4382.OilSealParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.OilSealParametricStudyTool]

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
    ) -> "List[_4382.OilSealParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.OilSealParametricStudyTool]

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
    ) -> "OilSealCompoundParametricStudyTool._Cast_OilSealCompoundParametricStudyTool":
        return self._Cast_OilSealCompoundParametricStudyTool(self)
