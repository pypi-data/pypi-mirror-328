"""SpecialisedAssemblyMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpecialisedAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5381,
        _5387,
        _5390,
        _5395,
        _5396,
        _5400,
        _5406,
        _5409,
        _5412,
        _5417,
        _5419,
        _5421,
        _5427,
        _5433,
        _5435,
        _5439,
        _5443,
        _5451,
        _5454,
        _5457,
        _5469,
        _5471,
        _5478,
        _5491,
        _5494,
        _5497,
        _5500,
        _5504,
        _5509,
        _5518,
        _5521,
        _5466,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyMultibodyDynamicsAnalysis")


class SpecialisedAssemblyMultibodyDynamicsAnalysis(
    _5375.AbstractAssemblyMultibodyDynamicsAnalysis
):
    """SpecialisedAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting SpecialisedAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
            parent: "SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5375.AbstractAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(_5375.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5466.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7548.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5381.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(
                _5381.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5387.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(_5387.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5390.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5395.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(_5395.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5396.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5400.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5406.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5409.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5412.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5417.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5419.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CVTMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5421.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5427.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5433.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5435.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(
                _5435.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5439.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5443.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443

            return self._parent._cast(_5443.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5451.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5454.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> (
            "_5457.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5469.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(
                _5469.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5471.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(_5471.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5478.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5491.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5494.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(_5494.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5497.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5500.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5504.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5509.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(_5509.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5518.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5521.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(_5521.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2476.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis(self)
