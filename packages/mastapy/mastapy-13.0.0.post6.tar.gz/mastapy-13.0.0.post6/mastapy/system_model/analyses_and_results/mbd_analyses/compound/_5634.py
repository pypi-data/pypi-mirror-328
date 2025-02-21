"""StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5495
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5533,
        _5561,
        _5587,
        _5593,
        _5563,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis"
)


class StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis(
    _5545.BevelGearMeshCompoundMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5545.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5545.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5533.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5561.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5587.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5593.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(_5563.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

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
    ) -> "List[_5495.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5495.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis(
            self
        )
