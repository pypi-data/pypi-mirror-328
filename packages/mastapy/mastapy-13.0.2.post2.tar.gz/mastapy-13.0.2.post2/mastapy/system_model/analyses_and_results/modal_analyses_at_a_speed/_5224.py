"""SpecialisedAssemblyModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5131,
        _5135,
        _5138,
        _5143,
        _5144,
        _5148,
        _5153,
        _5156,
        _5159,
        _5164,
        _5166,
        _5168,
        _5174,
        _5180,
        _5182,
        _5185,
        _5189,
        _5193,
        _5196,
        _5199,
        _5208,
        _5210,
        _5217,
        _5227,
        _5230,
        _5233,
        _5236,
        _5240,
        _5244,
        _5251,
        _5254,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysisAtASpeed")


class SpecialisedAssemblyModalAnalysisAtASpeed(
    _5125.AbstractAssemblyModalAnalysisAtASpeed
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
        ) -> "_5125.AbstractAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5125.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5131.AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(
                _5131.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5135.BeltDriveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5138.BevelDifferentialGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(
                _5138.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5143.BevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5144.BoltedJointModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.BoltedJointModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5148.ClutchModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ClutchModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5153.ConceptCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5156.ConceptGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5159.ConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5164.CouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5166.CVTModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.CVTModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5168.CycloidalAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5174.CylindricalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5180.FaceGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(_5180.FaceGearSetModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5182.FlexiblePinAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(_5182.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5185.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(_5185.GearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5189.HypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5193.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(
                _5193.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5196.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(
                _5196.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5199.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(
                _5199.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5208.PartToPartShearCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5210.PlanetaryGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5217.RollingRingAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5227.SpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5230.SpringDamperModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5233.StraightBevelDiffGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(
                _5233.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5236.StraightBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5240.SynchroniserModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.SynchroniserModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5244.TorqueConverterModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.TorqueConverterModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5251.WormGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5251,
            )

            return self._parent._cast(_5251.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyModalAnalysisAtASpeed._Cast_SpecialisedAssemblyModalAnalysisAtASpeed",
        ) -> "_5254.ZerolBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5254,
            )

            return self._parent._cast(_5254.ZerolBevelGearSetModalAnalysisAtASpeed)

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
    def assembly_design(self: Self) -> "_2483.SpecialisedAssembly":
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
