"""SpecialisedAssemblyDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SpecialisedAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6282,
        _6286,
        _6289,
        _6294,
        _6296,
        _6298,
        _6303,
        _6307,
        _6310,
        _6314,
        _6317,
        _6319,
        _6325,
        _6333,
        _6335,
        _6338,
        _6342,
        _6346,
        _6349,
        _6352,
        _6359,
        _6362,
        _6369,
        _6379,
        _6381,
        _6385,
        _6388,
        _6391,
        _6396,
        _6403,
        _6406,
        _6357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyDynamicAnalysis")


class SpecialisedAssemblyDynamicAnalysis(_6276.AbstractAssemblyDynamicAnalysis):
    """SpecialisedAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyDynamicAnalysis")

    class _Cast_SpecialisedAssemblyDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
            parent: "SpecialisedAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6276.AbstractAssemblyDynamicAnalysis":
            return self._parent._cast(_6276.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6357.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6282.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6286.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6289.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6294.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6296.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6298.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6303.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6307.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6310.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6314.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6317.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6319.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6325.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6333.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6335.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6338.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6342.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6346.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6349.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6352.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6359.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6362.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6369.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RollingRingAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6379.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6381.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6385.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6388.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6391.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6396.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6403.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "_6406.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.ZerolBevelGearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
        ) -> "SpecialisedAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyDynamicAnalysis.TYPE"
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
    ) -> "SpecialisedAssemblyDynamicAnalysis._Cast_SpecialisedAssemblyDynamicAnalysis":
        return self._Cast_SpecialisedAssemblyDynamicAnalysis(self)
