"""KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6478,
        _6481,
        _6467,
        _6473,
        _6443,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis(
    _6441.ConicalGearMeshCompoundDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6441.ConicalGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(_6441.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6467.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6473.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6443.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6478.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "_6481.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]

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
    ) -> "List[_6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis(
                self
            )
        )
