"""SpecialisedAssemblyMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpecialisedAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5382,
        _5388,
        _5391,
        _5396,
        _5397,
        _5401,
        _5407,
        _5410,
        _5413,
        _5418,
        _5420,
        _5422,
        _5428,
        _5434,
        _5436,
        _5440,
        _5444,
        _5452,
        _5455,
        _5458,
        _5470,
        _5472,
        _5479,
        _5492,
        _5495,
        _5498,
        _5501,
        _5505,
        _5510,
        _5519,
        _5522,
        _5467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyMultibodyDynamicsAnalysis")


class SpecialisedAssemblyMultibodyDynamicsAnalysis(
    _5376.AbstractAssemblyMultibodyDynamicsAnalysis
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
        ) -> "_5376.AbstractAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(_5376.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

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
        ) -> "_5382.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5388.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(_5388.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5391.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5396.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5397.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5401.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5407.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5410.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5413.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5418.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5420.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.CVTMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5422.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5428.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5434.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5436.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(
                _5436.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5440.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.GearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5444.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5452.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5455.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> (
            "_5458.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(
                _5458.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5470.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5472.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5479.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5492.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5495.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(_5495.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5498.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5501.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5505.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(_5505.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5510.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(_5510.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5519.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis)

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
