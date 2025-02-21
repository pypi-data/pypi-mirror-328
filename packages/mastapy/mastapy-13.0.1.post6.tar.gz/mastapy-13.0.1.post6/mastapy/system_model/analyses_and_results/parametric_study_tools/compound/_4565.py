"""VirtualComponentCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4520,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "VirtualComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4436
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4518,
        _4519,
        _4529,
        _4530,
        _4564,
        _4468,
        _4522,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="VirtualComponentCompoundParametricStudyTool")


class VirtualComponentCompoundParametricStudyTool(
    _4520.MountableComponentCompoundParametricStudyTool
):
    """VirtualComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundParametricStudyTool"
    )

    class _Cast_VirtualComponentCompoundParametricStudyTool:
        """Special nested class for casting VirtualComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
            parent: "VirtualComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4520.MountableComponentCompoundParametricStudyTool":
            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4468.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4522.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4518.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4519.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def point_load_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4529.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4530.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PowerLoadCompoundParametricStudyTool)

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "_4564.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
        ) -> "VirtualComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4436.VirtualComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool]

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
    ) -> "List[_4436.VirtualComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.VirtualComponentParametricStudyTool]

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
    ) -> "VirtualComponentCompoundParametricStudyTool._Cast_VirtualComponentCompoundParametricStudyTool":
        return self._Cast_VirtualComponentCompoundParametricStudyTool(self)
