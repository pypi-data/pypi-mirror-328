"""HypoidGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "HypoidGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315
    from mastapy.system_model.analyses_and_results.stability_analyses import _3827
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3930,
        _3956,
        _3962,
        _3932,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundStabilityAnalysis")


class HypoidGearMeshCompoundStabilityAnalysis(
    _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
):
    """HypoidGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_HypoidGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting HypoidGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
            parent: "HypoidGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(
                _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_3930.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_3956.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_3932.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
        ) -> "HypoidGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2315.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2315.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_3827.HypoidGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearMeshStabilityAnalysis]

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
    ) -> "List[_3827.HypoidGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearMeshStabilityAnalysis]

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
    ) -> "HypoidGearMeshCompoundStabilityAnalysis._Cast_HypoidGearMeshCompoundStabilityAnalysis":
        return self._Cast_HypoidGearMeshCompoundStabilityAnalysis(self)
