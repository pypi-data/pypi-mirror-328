"""AbstractAssemblyModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4946,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4871,
        _4872,
        _4875,
        _4878,
        _4883,
        _4884,
        _4888,
        _4893,
        _4896,
        _4899,
        _4904,
        _4906,
        _4908,
        _4914,
        _4921,
        _4923,
        _4926,
        _4930,
        _4934,
        _4937,
        _4940,
        _4949,
        _4951,
        _4958,
        _4961,
        _4965,
        _4968,
        _4971,
        _4974,
        _4977,
        _4981,
        _4985,
        _4992,
        _4995,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractAssemblyModalAnalysisAtAStiffness")


class AbstractAssemblyModalAnalysisAtAStiffness(_4946.PartModalAnalysisAtAStiffness):
    """AbstractAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
            parent: "AbstractAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4871.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(
                _4871.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4872.AssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(_4872.AssemblyModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4875.BeltDriveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4878.BevelDifferentialGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(
                _4878.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4883.BevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4884.BoltedJointModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.BoltedJointModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4888.ClutchModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ClutchModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4893.ConceptCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(_4893.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4896.ConceptGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4899.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4904.CouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4904,
            )

            return self._parent._cast(_4904.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4906.CVTModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.CVTModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4908.CycloidalAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4914.CylindricalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4921.FaceGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(_4921.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4923.FlexiblePinAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4923,
            )

            return self._parent._cast(
                _4923.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4926.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4926,
            )

            return self._parent._cast(_4926.GearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4930.HypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(_4930.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4934.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(
                _4934.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4937.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(
                _4937.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> (
            "_4940.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(
                _4940.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4949.PartToPartShearCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4951.PlanetaryGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(_4951.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4958.RollingRingAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4961.RootAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4965.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4968.SpiralBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(_4968.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4971.SpringDamperModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4974.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(
                _4974.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4977.StraightBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(
                _4977.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4981.SynchroniserModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(_4981.SynchroniserModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4985.TorqueConverterModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4992.WormGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(_4992.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "_4995.ZerolBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4995,
            )

            return self._parent._cast(_4995.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
        ) -> "AbstractAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "AbstractAssemblyModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyModalAnalysisAtAStiffness._Cast_AbstractAssemblyModalAnalysisAtAStiffness":
        return self._Cast_AbstractAssemblyModalAnalysisAtAStiffness(self)
