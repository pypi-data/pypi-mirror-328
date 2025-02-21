"""ComponentParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4296,
        _4297,
        _4300,
        _4303,
        _4307,
        _4309,
        _4310,
        _4312,
        _4315,
        _4317,
        _4322,
        _4325,
        _4328,
        _4331,
        _4333,
        _4337,
        _4340,
        _4343,
        _4345,
        _4346,
        _4354,
        _4356,
        _4358,
        _4361,
        _4363,
        _4365,
        _4369,
        _4372,
        _4375,
        _4377,
        _4378,
        _4380,
        _4381,
        _4394,
        _4398,
        _4399,
        _4400,
        _4401,
        _4402,
        _4406,
        _4408,
        _4409,
        _4413,
        _4416,
        _4419,
        _4422,
        _4424,
        _4425,
        _4426,
        _4428,
        _4429,
        _4432,
        _4433,
        _4434,
        _4435,
        _4437,
        _4440,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentParametricStudyTool")


class ComponentParametricStudyTool(_4392.PartParametricStudyTool):
    """ComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentParametricStudyTool")

    class _Cast_ComponentParametricStudyTool:
        """Special nested class for casting ComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            parent: "ComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4392.PartParametricStudyTool":
            return self._parent._cast(_4392.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4296.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4297.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4300.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4303.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4307.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4309.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(
                _4309.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4310.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4312.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BevelGearParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4315.BoltParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4317.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4322.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4325.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4328.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4331.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4333.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4337.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4340.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4343.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4345.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4346.DatumParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4354.ExternalCADModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4356.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FaceGearParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4358.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.FEPartParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4361.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4363.GuideDxfModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4365.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4369.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4372.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4375.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4377.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4378.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4380.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4381.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4394.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4398.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4399.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4400.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4401.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4402.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4406.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4408.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4409.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ShaftParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4413.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4416.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4419.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4422.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4424.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4425.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4426.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4428.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4429.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4432.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4433.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4434.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4435.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4437.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "_4440.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.ZerolBevelGearParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "ComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2444.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool":
        return self._Cast_ComponentParametricStudyTool(self)
