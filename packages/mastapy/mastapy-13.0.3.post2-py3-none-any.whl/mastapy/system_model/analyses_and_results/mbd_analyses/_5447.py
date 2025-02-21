"""CylindricalGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5458
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CylindricalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5470, _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshMultibodyDynamicsAnalysis")


class CylindricalGearMeshMultibodyDynamicsAnalysis(
    _5458.GearMeshMultibodyDynamicsAnalysis
):
    """CylindricalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
            parent: "CylindricalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5458.GearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5458.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
        ) -> "CylindricalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CylindricalGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stress_gear_a_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_a_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_b_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_b_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollDistanceLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollDistanceRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_a_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_a_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_b_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_b_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2329.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6885.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis(self)
