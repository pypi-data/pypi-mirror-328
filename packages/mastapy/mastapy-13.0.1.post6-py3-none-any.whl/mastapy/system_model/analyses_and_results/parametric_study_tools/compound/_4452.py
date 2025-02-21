"""BeltConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4508,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BeltConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4483,
        _4478,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BeltConnectionCompoundParametricStudyTool")


class BeltConnectionCompoundParametricStudyTool(
    _4508.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """BeltConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundParametricStudyTool"
    )

    class _Cast_BeltConnectionCompoundParametricStudyTool:
        """Special nested class for casting BeltConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
            parent: "BeltConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4508.InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4478.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "_4483.CVTBeltConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(
                _4483.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
        ) -> "BeltConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

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
    ) -> "List[_4305.BeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool]

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
    ) -> "List[_4305.BeltConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BeltConnectionParametricStudyTool]

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
    ) -> "BeltConnectionCompoundParametricStudyTool._Cast_BeltConnectionCompoundParametricStudyTool":
        return self._Cast_BeltConnectionCompoundParametricStudyTool(self)
