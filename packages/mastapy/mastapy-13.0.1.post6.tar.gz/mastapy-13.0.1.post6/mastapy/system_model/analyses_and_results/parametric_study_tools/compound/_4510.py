"""KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4476,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4513,
        _4516,
        _4502,
        _4508,
        _4478,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool(
    _4476.ConicalGearMeshCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4476.ConicalGearMeshCompoundParametricStudyTool":
            return self._parent._cast(_4476.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4502.GearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4508.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4478.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4513.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "_4516.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4369.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool(
            self
        )
