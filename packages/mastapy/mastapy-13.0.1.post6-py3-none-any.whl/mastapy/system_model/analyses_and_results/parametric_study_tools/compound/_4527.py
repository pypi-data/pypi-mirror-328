"""PlanetaryGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4492,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PlanetaryGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6934
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4503,
        _4541,
        _4443,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundParametricStudyTool")


class PlanetaryGearSetCompoundParametricStudyTool(
    _4492.CylindricalGearSetCompoundParametricStudyTool
):
    """PlanetaryGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundParametricStudyTool"
    )

    class _Cast_PlanetaryGearSetCompoundParametricStudyTool:
        """Special nested class for casting PlanetaryGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
            parent: "PlanetaryGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_4492.CylindricalGearSetCompoundParametricStudyTool":
            return self._parent._cast(
                _4492.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_4503.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_4541.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_4443.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "PlanetaryGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6934.PlanetaryGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4398.PlanetaryGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool]

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
    ) -> "List[_4398.PlanetaryGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool]

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
    ) -> "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool":
        return self._Cast_PlanetaryGearSetCompoundParametricStudyTool(self)
