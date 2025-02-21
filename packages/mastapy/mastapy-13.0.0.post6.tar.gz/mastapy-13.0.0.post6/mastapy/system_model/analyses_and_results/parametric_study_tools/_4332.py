"""CouplingConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4316,
        _4321,
        _4393,
        _4415,
        _4430,
        _4330,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingConnectionParametricStudyTool")


class CouplingConnectionParametricStudyTool(
    _4367.InterMountableComponentConnectionParametricStudyTool
):
    """CouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionParametricStudyTool"
    )

    class _Cast_CouplingConnectionParametricStudyTool:
        """Special nested class for casting CouplingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
            parent: "CouplingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4367.InterMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4367.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4330.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4316.ClutchConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.ClutchConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4321.ConceptCouplingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(
                _4321.ConceptCouplingConnectionParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4393.PartToPartShearCouplingConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(
                _4393.PartToPartShearCouplingConnectionParametricStudyTool
            )

        @property
        def spring_damper_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4415.SpringDamperConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpringDamperConnectionParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "_4430.TorqueConverterConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(
                _4430.TorqueConverterConnectionParametricStudyTool
            )

        @property
        def coupling_connection_parametric_study_tool(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
        ) -> "CouplingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "CouplingConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool":
        return self._Cast_CouplingConnectionParametricStudyTool(self)
