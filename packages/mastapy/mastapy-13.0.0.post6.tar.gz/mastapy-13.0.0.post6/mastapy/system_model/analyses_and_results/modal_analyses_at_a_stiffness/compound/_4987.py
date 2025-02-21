"""AbstractAssemblyCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5066,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4856,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4993,
        _4994,
        _4997,
        _5000,
        _5005,
        _5007,
        _5008,
        _5013,
        _5018,
        _5021,
        _5024,
        _5028,
        _5030,
        _5036,
        _5042,
        _5044,
        _5047,
        _5051,
        _5055,
        _5058,
        _5061,
        _5067,
        _5071,
        _5078,
        _5081,
        _5085,
        _5088,
        _5089,
        _5094,
        _5097,
        _5100,
        _5104,
        _5112,
        _5115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysisAtAStiffness")


class AbstractAssemblyCompoundModalAnalysisAtAStiffness(
    _5066.PartCompoundModalAnalysisAtAStiffness
):
    """AbstractAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
            parent: "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.PartCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_4993.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4993,
            )

            return self._parent._cast(
                _4993.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_4994.AssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(_4994.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_4997.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(_4997.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5000.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5007.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(
                _5007.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5008.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5008,
            )

            return self._parent._cast(_5008.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(
                _5013.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5018.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(_5024.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5028.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5028,
            )

            return self._parent._cast(_5028.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5030.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(
                _5030.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5042.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5044.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(
                _5044.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(
                _5071.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5078.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5081.RootAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5085.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5100.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5115.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractAssemblyCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4856.AbstractAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractAssemblyModalAnalysisAtAStiffness]

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
    ) -> "List[_4856.AbstractAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AbstractAssemblyModalAnalysisAtAStiffness]

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
    ) -> "AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness":
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness(self)
