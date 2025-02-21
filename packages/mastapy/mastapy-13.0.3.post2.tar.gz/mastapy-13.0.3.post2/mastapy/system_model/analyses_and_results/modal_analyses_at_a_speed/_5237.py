"""SpecialisedAssemblyModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2496
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
        _5148,
        _5151,
        _5156,
        _5157,
        _5161,
        _5166,
        _5169,
        _5172,
        _5177,
        _5179,
        _5181,
        _5187,
        _5193,
        _5195,
        _5198,
        _5202,
        _5206,
        _5209,
        _5212,
        _5221,
        _5223,
        _5230,
        _5240,
        _5243,
        _5246,
        _5249,
        _5253,
        _5257,
        _5264,
        _5267,
        _5218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysisAtASpeed")


class SpecialisedAssemblyModalAnalysisAtASpeed(
    _5138.AbstractAssemblyModalAnalysisAtASpeed
):
    """SpecialisedAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysisAtASpeed"
    )

    class _Cast_SpecialisedAssemblyModalAnalysisAtASpeed:
        """Special nested class for casting SpecialisedAssemblyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
            parent: "SpecialisedAssemblyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5138.AbstractAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5138.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5144.AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(
                _5144.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5148.BeltDriveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5151.BevelDifferentialGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(
                _5151.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5156.BevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5157.BoltedJointModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.BoltedJointModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5161.ClutchModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.ClutchModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5166.ConceptCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5169.ConceptGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5172.ConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5177.CouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5179.CVTModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(_5179.CVTModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5181.CycloidalAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(_5181.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5187.CylindricalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(_5187.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5193.FaceGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.FaceGearSetModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5195.FlexiblePinAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5198.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.GearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5202.HypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5206.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(
                _5206.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5209.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(
                _5209.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5212.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5221.PartToPartShearCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(
                _5221.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5223.PlanetaryGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5230.RollingRingAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5240.SpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5243.SpringDamperModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5246.StraightBevelDiffGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(
                _5246.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5249.StraightBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5249,
            )

            return self._parent._cast(_5249.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5253.SynchroniserModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.SynchroniserModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5257.TorqueConverterModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5257,
            )

            return self._parent._cast(_5257.TorqueConverterModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5264.WormGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5264,
            )

            return self._parent._cast(_5264.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5267.ZerolBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5267,
            )

            return self._parent._cast(_5267.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2496.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed":
        return self._Cast_SpecialisedAssemblyModalAnalysisAtASpeed(self)
