"""ZerolBevelGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.stability_analyses import _3894
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3902,
        _3930,
        _3956,
        _3962,
        _3932,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundStabilityAnalysis")


class ZerolBevelGearMeshCompoundStabilityAnalysis(
    _3914.BevelGearMeshCompoundStabilityAnalysis
):
    """ZerolBevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_ZerolBevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
            parent: "ZerolBevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3914.BevelGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3914.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(
                _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3930.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3956.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3932.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
        ) -> "ZerolBevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_3894.ZerolBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearMeshStabilityAnalysis]

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
    ) -> "List[_3894.ZerolBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearMeshStabilityAnalysis]

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
    ) -> "ZerolBevelGearMeshCompoundStabilityAnalysis._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_ZerolBevelGearMeshCompoundStabilityAnalysis(self)
