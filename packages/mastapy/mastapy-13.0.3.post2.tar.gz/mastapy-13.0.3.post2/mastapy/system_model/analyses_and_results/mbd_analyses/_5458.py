"""GearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _69
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5401,
        _5410,
        _5415,
        _5429,
        _5432,
        _5447,
        _5453,
        _5463,
        _5471,
        _5474,
        _5477,
        _5511,
        _5517,
        _5520,
        _5538,
        _5541,
        _5435,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearMeshMultibodyDynamicsAnalysis")


class GearMeshMultibodyDynamicsAnalysis(
    _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """GearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshMultibodyDynamicsAnalysis")

    class _Cast_GearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
            parent: "GearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5410.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(
                _5410.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5415.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5429.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5432.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5447.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5453.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(_5453.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5463.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5471.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5474.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(
                _5474.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> (
            "_5477.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5511.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5517.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(
                _5517.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5520.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(
                _5520.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5538.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5538

            return self._parent._cast(_5538.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "_5541.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5541

            return self._parent._cast(_5541.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
        ) -> "GearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_sliding_velocity_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageSlidingVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def average_sliding_velocity_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageSlidingVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFrictionRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_status(self: Self) -> "_69.GearMeshContactStatus":
        """mastapy.nodal_analysis.GearMeshContactStatus

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.GearMeshContactStatus"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._69", "GearMeshContactStatus"
        )(value)

    @property
    def equivalent_misalignment_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignmentLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentMisalignmentRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_total(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImpactPowerTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDueToTiltLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDueToTiltRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationTransverseToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationTransverseToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_total(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergyTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingSpeedGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingSpeedGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2333.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis":
        return self._Cast_GearMeshMultibodyDynamicsAnalysis(self)
