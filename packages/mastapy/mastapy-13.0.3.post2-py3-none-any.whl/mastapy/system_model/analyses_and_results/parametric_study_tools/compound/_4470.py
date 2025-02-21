"""AGMAGleasonConicalGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4498,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4323
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4477,
        _4482,
        _4528,
        _4565,
        _4571,
        _4574,
        _4592,
        _4524,
        _4562,
        _4464,
        _4543,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundParametricStudyTool")


class AGMAGleasonConicalGearSetCompoundParametricStudyTool(
    _4498.ConicalGearSetCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
            parent: "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4498.ConicalGearSetCompoundParametricStudyTool":
            return self._parent._cast(_4498.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4524.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4562.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4464.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4543.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4477.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(
                _4477.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4482.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.BevelGearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4528.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.HypoidGearSetCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4565.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(
                _4565.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4571.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4574.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(
                _4574.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "_4592.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4592,
            )

            return self._parent._cast(
                _4592.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
        ) -> "AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4323.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4323.AGMAGleasonConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearSetParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearSetCompoundParametricStudyTool(self)
