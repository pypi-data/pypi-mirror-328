"""KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5314,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5186,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5280,
        _5306,
        _5312,
        _5282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed(
    _5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ):
            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5306.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5282.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2319.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "List[_5186.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed]

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
    ) -> "List[_5186.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed(
            self
        )
