"""SpecialisedAssemblyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpecialisedAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6413,
        _6417,
        _6420,
        _6425,
        _6427,
        _6428,
        _6433,
        _6438,
        _6441,
        _6444,
        _6448,
        _6450,
        _6456,
        _6462,
        _6464,
        _6467,
        _6471,
        _6475,
        _6478,
        _6481,
        _6487,
        _6491,
        _6498,
        _6508,
        _6509,
        _6514,
        _6517,
        _6520,
        _6524,
        _6532,
        _6535,
        _6486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundDynamicAnalysis")


class SpecialisedAssemblyCompoundDynamicAnalysis(
    _6407.AbstractAssemblyCompoundDynamicAnalysis
):
    """SpecialisedAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
            parent: "SpecialisedAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6407.AbstractAssemblyCompoundDynamicAnalysis":
            return self._parent._cast(_6407.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6486.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6413.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(
                _6413.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6417.BeltDriveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(_6417.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6420.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6425.BevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(_6425.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6427.BoltedJointCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6428.ClutchCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6433.ConceptCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6438.ConceptGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6441.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6444.CouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6448.CVTCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6450.CycloidalAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6456.CylindricalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6462.FaceGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6464.FlexiblePinAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6467.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6471.HypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6475.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6478.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6481.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6487.PartToPartShearCouplingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6491.PlanetaryGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6498.RollingRingAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(_6498.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6508.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6509.SpringDamperCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6514.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(
                _6514.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6517.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6520.SynchroniserCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6524.TorqueConverterCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6532.WormGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "_6535.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
        ) -> "SpecialisedAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6376.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "List[_6376.SpecialisedAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundDynamicAnalysis._Cast_SpecialisedAssemblyCompoundDynamicAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundDynamicAnalysis(self)
