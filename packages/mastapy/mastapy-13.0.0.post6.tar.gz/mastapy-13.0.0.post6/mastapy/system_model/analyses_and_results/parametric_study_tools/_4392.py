"""PartParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1859, _1867, _1865
    from mastapy.system_model.part_model import _2468
    from mastapy.utility_gui import _1850
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4387,
        _4295,
        _4296,
        _4297,
        _4300,
        _4301,
        _4302,
        _4303,
        _4305,
        _4307,
        _4308,
        _4309,
        _4310,
        _4312,
        _4313,
        _4314,
        _4315,
        _4317,
        _4318,
        _4320,
        _4322,
        _4323,
        _4325,
        _4326,
        _4328,
        _4329,
        _4331,
        _4333,
        _4334,
        _4336,
        _4337,
        _4338,
        _4340,
        _4343,
        _4344,
        _4345,
        _4346,
        _4354,
        _4356,
        _4357,
        _4358,
        _4359,
        _4361,
        _4362,
        _4363,
        _4365,
        _4366,
        _4369,
        _4370,
        _4372,
        _4373,
        _4375,
        _4376,
        _4377,
        _4378,
        _4380,
        _4381,
        _4394,
        _4395,
        _4397,
        _4398,
        _4399,
        _4400,
        _4401,
        _4402,
        _4404,
        _4406,
        _4407,
        _4408,
        _4409,
        _4411,
        _4413,
        _4414,
        _4416,
        _4417,
        _4419,
        _4420,
        _4422,
        _4423,
        _4424,
        _4425,
        _4426,
        _4427,
        _4428,
        _4429,
        _4431,
        _4432,
        _4433,
        _4434,
        _4435,
        _4437,
        _4438,
        _4440,
        _4441,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartParametricStudyTool",)


Self = TypeVar("Self", bound="PartParametricStudyTool")


class PartParametricStudyTool(_7544.PartAnalysisCase):
    """PartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartParametricStudyTool")

    class _Cast_PartParametricStudyTool:
        """Special nested class for casting PartParametricStudyTool to subclasses."""

        def __init__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
            parent: "PartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_7544.PartAnalysisCase":
            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4295.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4296.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4297.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4300.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4301.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(
                _4301.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4302.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(_4302.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4303.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4305.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4307.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4308.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4309.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(
                _4309.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4310.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4312.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4313.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4314.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4315.BoltParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4317.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4318.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4320.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4322.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4323.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4325.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4326.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4328.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4329.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4331.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4333.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4334.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4336.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4337.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4338.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4340.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4343.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4344.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4345.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4346.DatumParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4354.ExternalCADModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4356.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4357.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4358.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4359.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4361.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4362.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4363.GuideDxfModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4365.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4366.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4369.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4370.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4372.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4373.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4375.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4376.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4377.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4378.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4380.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4381.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4394.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(
                _4394.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4395.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4397.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4398.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4399.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4400.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4401.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4402.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4404.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4406.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4407.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4408.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4409.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4411.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4413.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4414.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4416.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4417.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4419.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4420.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4422.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4423.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4424.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4425.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4426.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4427.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4428.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4429.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4431.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4432.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4433.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4434.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4435.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4437.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4438.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4440.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4441.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.ZerolBevelGearSetParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "PartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_of_experiments_chart(self: Self) -> "_1859.NDChartDefinition":
        """mastapy.utility_gui.charts.NDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignOfExperimentsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_2d(self: Self) -> "_1867.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart2D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_3d(self: Self) -> "_1865.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def data_logger(self: Self) -> "_1850.DataLoggerWithCharts":
        """mastapy.utility_gui.DataLoggerWithCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool(self: Self) -> "_4387.ParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartParametricStudyTool._Cast_PartParametricStudyTool":
        return self._Cast_PartParametricStudyTool(self)
