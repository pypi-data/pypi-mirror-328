"""ConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5464,
        _5378,
        _5379,
        _5386,
        _5388,
        _5393,
        _5398,
        _5402,
        _5404,
        _5407,
        _5410,
        _5415,
        _5418,
        _5422,
        _5424,
        _5425,
        _5431,
        _5436,
        _5441,
        _5448,
        _5449,
        _5452,
        _5455,
        _5467,
        _5470,
        _5477,
        _5479,
        _5486,
        _5489,
        _5492,
        _5495,
        _5498,
        _5507,
        _5516,
        _5519,
    )
    from mastapy.math_utility.convergence import _1575
    from mastapy.system_model.analyses_and_results.analysis_cases import _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectionMultibodyDynamicsAnalysis")


class ConnectionMultibodyDynamicsAnalysis(_7541.ConnectionTimeSeriesLoadAnalysisCase):
    """ConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionMultibodyDynamicsAnalysis")

    class _Cast_ConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
            parent: "ConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionTimeSeriesLoadAnalysisCase":
            return self._parent._cast(_7541.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5378.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5379.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5386.BeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(_5386.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5388.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5393.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5398.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5402.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(_5402.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5404.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5407.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5410.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5415.CouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5418.CVTBeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(
                _5422.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5424.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(
                _5424.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5425.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5431.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5436.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5441.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5448.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5449.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5452.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5455.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5467.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5477.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5479.RollingRingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5486.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5489.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5492.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5495.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5498.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5507.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(
                _5507.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5516.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "_5519.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
        ) -> "ConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self: Self) -> "_2272.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2272.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def multibody_dynamics_analysis(self: Self) -> "_5464.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1575.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis"
    ):
        return self._Cast_ConnectionMultibodyDynamicsAnalysis(self)
