"""AbstractShaftOrHousingParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractShaftOrHousingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4298,
        _4341,
        _4359,
        _4410,
        _4393,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingParametricStudyTool")


class AbstractShaftOrHousingParametricStudyTool(_4321.ComponentParametricStudyTool):
    """AbstractShaftOrHousingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingParametricStudyTool"
    )

    class _Cast_AbstractShaftOrHousingParametricStudyTool:
        """Special nested class for casting AbstractShaftOrHousingParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
            parent: "AbstractShaftOrHousingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4321.ComponentParametricStudyTool":
            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4393.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4298.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractShaftParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4341.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CycloidalDiscParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4359.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.FEPartParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "_4410.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.ShaftParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
        ) -> "AbstractShaftOrHousingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingParametricStudyTool._Cast_AbstractShaftOrHousingParametricStudyTool":
        return self._Cast_AbstractShaftOrHousingParametricStudyTool(self)
