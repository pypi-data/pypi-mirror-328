"""ConnectionTimeSeriesLoadAnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionTimeSeriesLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5379,
        _5380,
        _5387,
        _5389,
        _5394,
        _5399,
        _5403,
        _5405,
        _5408,
        _5411,
        _5414,
        _5416,
        _5419,
        _5423,
        _5425,
        _5426,
        _5432,
        _5437,
        _5442,
        _5449,
        _5450,
        _5453,
        _5456,
        _5468,
        _5471,
        _5478,
        _5480,
        _5487,
        _5490,
        _5493,
        _5496,
        _5499,
        _5508,
        _5517,
        _5520,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionTimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="ConnectionTimeSeriesLoadAnalysisCase")


class ConnectionTimeSeriesLoadAnalysisCase(_7538.ConnectionAnalysisCase):
    """ConnectionTimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionTimeSeriesLoadAnalysisCase")

    class _Cast_ConnectionTimeSeriesLoadAnalysisCase:
        """Special nested class for casting ConnectionTimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
            parent: "ConnectionTimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def connection_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_7538.ConnectionAnalysisCase":
            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> (
            "_5379.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5387.BeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(_5387.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5389.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5394.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5399.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5403.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5405.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(
                _5405.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5408.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5411.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5414.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5416.CouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5419.CVTBeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5423.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(
                _5423.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5425.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5426.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5432.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5437.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5442.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5453.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> (
            "_5456.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(
                _5456.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5468.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(
                _5468.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5471.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5478.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5480.RollingRingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(
                _5480.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5487.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5490.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(
                _5490.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5493.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5496.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(
                _5496.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5499.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5508.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5517.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5520.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "ConnectionTimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
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
        self: Self, instance_to_wrap: "ConnectionTimeSeriesLoadAnalysisCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase":
        return self._Cast_ConnectionTimeSeriesLoadAnalysisCase(self)
