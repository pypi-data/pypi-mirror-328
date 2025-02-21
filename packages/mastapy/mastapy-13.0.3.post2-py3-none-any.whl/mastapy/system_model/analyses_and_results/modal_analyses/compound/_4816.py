"""KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4664
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4819,
        _4822,
        _4808,
        _4814,
        _4784,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis(
    _4782.ConicalGearMeshCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4782.ConicalGearMeshCompoundModalAnalysis":
            return self._parent._cast(_4782.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4808.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4814.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(
                _4814.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(
                _4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "_4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(
                _4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4664.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

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
    ) -> "List[_4664.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis(
            self
        )
