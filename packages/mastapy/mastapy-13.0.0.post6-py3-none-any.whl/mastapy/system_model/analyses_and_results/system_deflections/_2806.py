"""SpecialisedAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpecialisedAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.power_flows import _4134
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2690,
        _2700,
        _2702,
        _2707,
        _2709,
        _2713,
        _2719,
        _2721,
        _2725,
        _2731,
        _2734,
        _2735,
        _2742,
        _2743,
        _2744,
        _2755,
        _2758,
        _2760,
        _2764,
        _2769,
        _2772,
        _2775,
        _2788,
        _2797,
        _2808,
        _2812,
        _2814,
        _2817,
        _2824,
        _2830,
        _2837,
        _2840,
        _2785,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7546,
        _7547,
        _7544,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblySystemDeflection")


class SpecialisedAssemblySystemDeflection(_2685.AbstractAssemblySystemDeflection):
    """SpecialisedAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblySystemDeflection")

    class _Cast_SpecialisedAssemblySystemDeflection:
        """Special nested class for casting SpecialisedAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
            parent: "SpecialisedAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2685.AbstractAssemblySystemDeflection":
            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2785.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7546.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2690.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2700.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2702.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2707.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2709.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2713.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2719.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2721.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2725.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2731.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2734.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2735.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2742.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2743.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2744.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2755.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2758.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2760.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2764.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2769.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2772.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2775.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2788.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2797.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2808.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2812.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2814.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2817.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2824.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2830.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2837.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "_2840.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.ZerolBevelGearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
        ) -> "SpecialisedAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblySystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4134.SpecialisedAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpecialisedAssemblySystemDeflection._Cast_SpecialisedAssemblySystemDeflection"
    ):
        return self._Cast_SpecialisedAssemblySystemDeflection(self)
