"""RingPinsToDiscConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4529,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2361
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4425
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4499,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundParametricStudyTool")


class RingPinsToDiscConnectionCompoundParametricStudyTool(
    _4529.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """RingPinsToDiscConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCompoundParametricStudyTool"
    )

    class _Cast_RingPinsToDiscConnectionCompoundParametricStudyTool:
        """Special nested class for casting RingPinsToDiscConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
            parent: "RingPinsToDiscConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "_4529.InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4529.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "_4499.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
        ) -> "RingPinsToDiscConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2361.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2361.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

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
    ) -> "List[_4425.RingPinsToDiscConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RingPinsToDiscConnectionParametricStudyTool]

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
    ) -> "List[_4425.RingPinsToDiscConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RingPinsToDiscConnectionParametricStudyTool]

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
    ) -> "RingPinsToDiscConnectionCompoundParametricStudyTool._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool":
        return self._Cast_RingPinsToDiscConnectionCompoundParametricStudyTool(self)
