"""MountableComponentCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4467,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "MountableComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4380
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4446,
        _4450,
        _4453,
        _4456,
        _4457,
        _4458,
        _4465,
        _4470,
        _4471,
        _4474,
        _4478,
        _4481,
        _4484,
        _4489,
        _4492,
        _4495,
        _4500,
        _4504,
        _4508,
        _4511,
        _4514,
        _4517,
        _4518,
        _4520,
        _4524,
        _4527,
        _4528,
        _4529,
        _4530,
        _4531,
        _4534,
        _4538,
        _4541,
        _4546,
        _4547,
        _4550,
        _4553,
        _4554,
        _4556,
        _4557,
        _4558,
        _4561,
        _4562,
        _4563,
        _4564,
        _4565,
        _4568,
        _4521,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="MountableComponentCompoundParametricStudyTool")


class MountableComponentCompoundParametricStudyTool(
    _4467.ComponentCompoundParametricStudyTool
):
    """MountableComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundParametricStudyTool"
    )

    class _Cast_MountableComponentCompoundParametricStudyTool:
        """Special nested class for casting MountableComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
            parent: "MountableComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4467.ComponentCompoundParametricStudyTool":
            return self._parent._cast(_4467.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4521.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4446.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(
                _4446.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bearing_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4450.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(_4450.BearingCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4453.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4456.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4457.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4458.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BevelGearCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4465.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4470.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4471.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4474.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConicalGearCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4478.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4481.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4484.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CVTPulleyCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4489.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4492.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(
                _4492.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def face_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4495.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.FaceGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4500.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4504.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4508.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4511.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4514.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4517.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4518.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(
                _4518.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4520.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(_4520.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4524.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(
                _4524.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4527.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4528.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4529.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4530.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4531.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4534.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(_4534.RollingRingCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4538.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4541.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(_4541.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4546.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(_4546.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4547.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4550.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4553.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4554.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4556.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4557.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(_4557.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4558.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4561.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4562.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4563.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(_4563.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4564.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4565.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "_4568.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
        ) -> "MountableComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool",
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
        instance_to_wrap: "MountableComponentCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4380.MountableComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4380.MountableComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.MountableComponentParametricStudyTool]

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
    ) -> "MountableComponentCompoundParametricStudyTool._Cast_MountableComponentCompoundParametricStudyTool":
        return self._Cast_MountableComponentCompoundParametricStudyTool(self)
