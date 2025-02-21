"""BevelDifferentialPlanetGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4453,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6825
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4458,
        _4446,
        _4474,
        _4500,
        _4519,
        _4467,
        _4521,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundParametricStudyTool")


class BevelDifferentialPlanetGearCompoundParametricStudyTool(
    _4453.BevelDifferentialGearCompoundParametricStudyTool
):
    """BevelDifferentialPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
            parent: "BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4453.BevelDifferentialGearCompoundParametricStudyTool":
            return self._parent._cast(
                _4453.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4458.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4446.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(
                _4446.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4474.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4500.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4519.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4467.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_4521.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
        ) -> "BevelDifferentialPlanetGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6825.BevelDifferentialPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase

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
    ) -> "List[_4309.BevelDifferentialPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialPlanetGearParametricStudyTool]

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
    ) -> "List[_4309.BevelDifferentialPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialPlanetGearParametricStudyTool]

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
    ) -> "BevelDifferentialPlanetGearCompoundParametricStudyTool._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool":
        return self._Cast_BevelDifferentialPlanetGearCompoundParametricStudyTool(self)
