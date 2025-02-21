"""PlanetaryConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4539,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PlanetaryConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4445,
        _4477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundParametricStudyTool")


class PlanetaryConnectionCompoundParametricStudyTool(
    _4539.ShaftToMountableComponentConnectionCompoundParametricStudyTool
):
    """PlanetaryConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundParametricStudyTool"
    )

    class _Cast_PlanetaryConnectionCompoundParametricStudyTool:
        """Special nested class for casting PlanetaryConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
            parent: "PlanetaryConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_4539.ShaftToMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4539.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_4445.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_4477.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
        ) -> "PlanetaryConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "PlanetaryConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

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
    ) -> "List[_4396.PlanetaryConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryConnectionParametricStudyTool]

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
    ) -> "List[_4396.PlanetaryConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryConnectionParametricStudyTool]

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
    ) -> "PlanetaryConnectionCompoundParametricStudyTool._Cast_PlanetaryConnectionCompoundParametricStudyTool":
        return self._Cast_PlanetaryConnectionCompoundParametricStudyTool(self)
