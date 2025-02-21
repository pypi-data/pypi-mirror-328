"""MountableComponentPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "MountableComponentPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4037,
        _4040,
        _4044,
        _4046,
        _4047,
        _4049,
        _4054,
        _4059,
        _4062,
        _4065,
        _4068,
        _4070,
        _4074,
        _4081,
        _4083,
        _4087,
        _4094,
        _4098,
        _4102,
        _4105,
        _4108,
        _4110,
        _4111,
        _4113,
        _4116,
        _4120,
        _4121,
        _4124,
        _4125,
        _4126,
        _4130,
        _4132,
        _4137,
        _4140,
        _4143,
        _4146,
        _4148,
        _4149,
        _4150,
        _4151,
        _4153,
        _4157,
        _4158,
        _4159,
        _4160,
        _4162,
        _4165,
        _4114,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentPowerFlow")


class MountableComponentPowerFlow(_4057.ComponentPowerFlow):
    """MountableComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentPowerFlow")

    class _Cast_MountableComponentPowerFlow:
        """Special nested class for casting MountableComponentPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            parent: "MountableComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4114.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4037.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4040.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4044.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4046.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4047.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4049.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4054.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4059.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4062.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4065.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def connector_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4068.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4070.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4074.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTPulleyPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4081.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4083.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4087.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.FaceGearPowerFlow)

        @property
        def gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4094.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4098.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4102.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(
                _4102.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4105.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4108.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(
                _4108.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4110.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4111.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MeasurementComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4113.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4116.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4120.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4121.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4124.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4125.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4126.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4130.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4132.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.ShaftHubConnectionPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4137.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4140.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4143.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4146.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4148.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4149.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4150.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4151.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4153.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4157.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4158.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4159.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4160.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4162.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4165.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.ZerolBevelGearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "MountableComponentPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow":
        return self._Cast_MountableComponentPowerFlow(self)
