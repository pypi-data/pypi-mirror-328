"""ConceptCouplingConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConceptCouplingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2364
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionParametricStudyTool")


class ConceptCouplingConnectionParametricStudyTool(
    _4354.CouplingConnectionParametricStudyTool
):
    """ConceptCouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionParametricStudyTool"
    )

    class _Cast_ConceptCouplingConnectionParametricStudyTool:
        """Special nested class for casting ConceptCouplingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
            parent: "ConceptCouplingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_parametric_study_tool(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_4354.CouplingConnectionParametricStudyTool":
            return self._parent._cast(_4354.CouplingConnectionParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
        ) -> "ConceptCouplingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool",
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
        instance_to_wrap: "ConceptCouplingConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2364.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6860.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2738.ConceptCouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool":
        return self._Cast_ConceptCouplingConnectionParametricStudyTool(self)
