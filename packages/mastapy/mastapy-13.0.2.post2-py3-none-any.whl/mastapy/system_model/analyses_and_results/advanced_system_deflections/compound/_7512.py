"""SpecialisedAssemblyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7414,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7382,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7420,
        _7424,
        _7427,
        _7432,
        _7434,
        _7435,
        _7440,
        _7445,
        _7448,
        _7451,
        _7455,
        _7457,
        _7463,
        _7469,
        _7471,
        _7474,
        _7478,
        _7482,
        _7485,
        _7488,
        _7494,
        _7498,
        _7505,
        _7515,
        _7516,
        _7521,
        _7524,
        _7527,
        _7531,
        _7539,
        _7542,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundAdvancedSystemDeflection")


class SpecialisedAssemblyCompoundAdvancedSystemDeflection(
    _7414.AbstractAssemblyCompoundAdvancedSystemDeflection
):
    """SpecialisedAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7414.AbstractAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7414.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7424.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(_7424.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7432.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7434.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(_7434.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7435.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7440.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7445.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7448.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(
                _7448.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7451.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(_7451.CouplingCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7455.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(_7455.CVTCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7457.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7463.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(
                _7463.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7469.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(_7469.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7471.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7474.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(_7474.GearSetCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7478.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7494.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(
                _7494.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7498.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(
                _7498.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7505.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7516.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7524.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7527.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7531.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7539.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7539,
            )

            return self._parent._cast(_7539.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7382.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "List[_7382.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection(self)
