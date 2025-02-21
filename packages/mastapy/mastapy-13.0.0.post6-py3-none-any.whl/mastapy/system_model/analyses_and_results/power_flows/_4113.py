"""PartPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4121,
        _4032,
        _4033,
        _4034,
        _4037,
        _4038,
        _4039,
        _4040,
        _4042,
        _4044,
        _4045,
        _4046,
        _4047,
        _4049,
        _4050,
        _4051,
        _4052,
        _4054,
        _4055,
        _4057,
        _4059,
        _4060,
        _4062,
        _4063,
        _4065,
        _4066,
        _4068,
        _4070,
        _4071,
        _4073,
        _4074,
        _4075,
        _4078,
        _4081,
        _4082,
        _4083,
        _4084,
        _4085,
        _4087,
        _4088,
        _4090,
        _4091,
        _4093,
        _4094,
        _4095,
        _4097,
        _4098,
        _4101,
        _4102,
        _4104,
        _4105,
        _4107,
        _4108,
        _4109,
        _4110,
        _4111,
        _4112,
        _4115,
        _4116,
        _4118,
        _4119,
        _4120,
        _4123,
        _4124,
        _4125,
        _4127,
        _4129,
        _4130,
        _4131,
        _4132,
        _4134,
        _4136,
        _4137,
        _4139,
        _4140,
        _4142,
        _4143,
        _4145,
        _4146,
        _4147,
        _4148,
        _4149,
        _4150,
        _4151,
        _4152,
        _4155,
        _4156,
        _4157,
        _4158,
        _4159,
        _4161,
        _4162,
        _4164,
        _4165,
    )
    from mastapy.system_model.drawing import _2254
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartPowerFlow",)


Self = TypeVar("Self", bound="PartPowerFlow")


class PartPowerFlow(_7547.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartPowerFlow")

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(
            self: "PartPowerFlow._Cast_PartPowerFlow", parent: "PartPowerFlow"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4032.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4033.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4034.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4037.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4038.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4039.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4040.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4042.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4044.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4045.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4046.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4047.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4049.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4050.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4051.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4052.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4054.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4055.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4057.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4059.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4060.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4062.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4063.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4065.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4066.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4068.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4070.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4071.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4073.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4074.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4075.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4078.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4081.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4082.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4083.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4084.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4085.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4087.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4088.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4090.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4091.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4093.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4094.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4095.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4097.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4098.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4101.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4102.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(
                _4102.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4104.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4105.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4107.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(
                _4107.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4108.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(
                _4108.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4109.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4110.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4111.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4112.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4115.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4116.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4118.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4119.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4120.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4123.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4124.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4125.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4127.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4129.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4130.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4131.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4132.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4134.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4136.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4137.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4139.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4140.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4142.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4143.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4145.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4146.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4147.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4148.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4149.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4150.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4151.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4152.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4155.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4156.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4157.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4158.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4159.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4161.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4162.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4164.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4165.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "PartPowerFlow":
            return self._parent

        def __getattr__(self: "PartPowerFlow._Cast_PartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2468.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4121.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2254.PowerFlowViewable":
        """mastapy.system_model.drawing.PowerFlowViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartPowerFlow._Cast_PartPowerFlow":
        return self._Cast_PartPowerFlow(self)
