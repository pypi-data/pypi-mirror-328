"""ConceptCouplingConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4481,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4508,
        _4478,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundParametricStudyTool")


class ConceptCouplingConnectionCompoundParametricStudyTool(
    _4481.CouplingConnectionCompoundParametricStudyTool
):
    """ConceptCouplingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundParametricStudyTool"
    )

    class _Cast_ConceptCouplingConnectionCompoundParametricStudyTool:
        """Special nested class for casting ConceptCouplingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
            parent: "ConceptCouplingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4481.CouplingConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4481.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4508.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_4478.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
        ) -> "ConceptCouplingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2344.ConceptCouplingConnection":
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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4322.ConceptCouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4322.ConceptCouplingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptCouplingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCompoundParametricStudyTool._Cast_ConceptCouplingConnectionCompoundParametricStudyTool":
        return self._Cast_ConceptCouplingConnectionCompoundParametricStudyTool(self)
