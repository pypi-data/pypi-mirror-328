"""PartToPartShearCouplingConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartToPartShearCouplingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4352,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionParametricStudyTool")


class PartToPartShearCouplingConnectionParametricStudyTool(
    _4354.CouplingConnectionParametricStudyTool
):
    """PartToPartShearCouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionParametricStudyTool"
    )

    class _Cast_PartToPartShearCouplingConnectionParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
            parent: "PartToPartShearCouplingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_4354.CouplingConnectionParametricStudyTool":
            return self._parent._cast(_4354.CouplingConnectionParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_4389.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(
                _4389.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_4352.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
        ) -> "PartToPartShearCouplingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

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
    ) -> "List[_2807.PartToPartShearCouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection]

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
    ) -> "PartToPartShearCouplingConnectionParametricStudyTool._Cast_PartToPartShearCouplingConnectionParametricStudyTool":
        return self._Cast_PartToPartShearCouplingConnectionParametricStudyTool(self)
