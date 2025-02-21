"""ComponentCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4246
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4057
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4168,
        _4169,
        _4171,
        _4175,
        _4178,
        _4181,
        _4182,
        _4183,
        _4186,
        _4190,
        _4195,
        _4196,
        _4199,
        _4203,
        _4206,
        _4209,
        _4212,
        _4214,
        _4217,
        _4218,
        _4219,
        _4220,
        _4223,
        _4225,
        _4228,
        _4229,
        _4233,
        _4236,
        _4239,
        _4242,
        _4243,
        _4244,
        _4245,
        _4249,
        _4252,
        _4253,
        _4254,
        _4255,
        _4256,
        _4259,
        _4262,
        _4263,
        _4266,
        _4271,
        _4272,
        _4275,
        _4278,
        _4279,
        _4281,
        _4282,
        _4283,
        _4286,
        _4287,
        _4288,
        _4289,
        _4290,
        _4293,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="ComponentCompoundPowerFlow")


class ComponentCompoundPowerFlow(_4246.PartCompoundPowerFlow):
    """ComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundPowerFlow")

    class _Cast_ComponentCompoundPowerFlow:
        """Special nested class for casting ComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            parent: "ComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4168.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4169.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4171.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4175.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4178.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4181.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(
                _4181.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4182.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4183.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BevelGearCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4186.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.BoltCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4190.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4195.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4196.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4199.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4203.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4206.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4209.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4212.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4214.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4217.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4218.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4219.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4220.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.FaceGearCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4223.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.FEPartCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4225.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4228.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4229.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4233.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4236.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4239.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(
                _4239.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4242.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4243.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4244.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4245.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4249.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4252.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4253.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4254.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4255.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4256.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4259.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.RollingRingCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4262.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4263.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4266.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4271.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4272.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4275.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4278.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4279.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4281.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4282.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4283.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4286.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4287.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4288.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4289.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4290.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4293.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.ZerolBevelGearCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "ComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4057.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4057.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow":
        return self._Cast_ComponentCompoundPowerFlow(self)
