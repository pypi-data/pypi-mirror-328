"""SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7140,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7109,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7146,
        _7150,
        _7153,
        _7158,
        _7160,
        _7161,
        _7166,
        _7171,
        _7174,
        _7177,
        _7181,
        _7183,
        _7189,
        _7195,
        _7197,
        _7200,
        _7204,
        _7208,
        _7211,
        _7214,
        _7220,
        _7224,
        _7231,
        _7241,
        _7242,
        _7247,
        _7250,
        _7253,
        _7257,
        _7265,
        _7268,
        _7219,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7140.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7140.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7146,
            )

            return self._parent._cast(
                _7146.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7160.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7171.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7177.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7181.CVTCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7183.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7189.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7195.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7197.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7200.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7204.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7211.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7224.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7231.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7241.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7242.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7247.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7250.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7253.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7257.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7265.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7268.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7109.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7109.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
