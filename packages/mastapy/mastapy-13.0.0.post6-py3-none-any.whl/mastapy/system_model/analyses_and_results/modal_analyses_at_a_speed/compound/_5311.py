"""InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5281,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5181,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5251,
        _5255,
        _5258,
        _5263,
        _5268,
        _5273,
        _5276,
        _5279,
        _5284,
        _5286,
        _5294,
        _5300,
        _5305,
        _5309,
        _5313,
        _5316,
        _5319,
        _5327,
        _5336,
        _5339,
        _5346,
        _5349,
        _5352,
        _5355,
        _5364,
        _5370,
        _5373,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"
)


class InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5281.ConnectionCompoundModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5281.ConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5281.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5251.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(
                _5251.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5255.BeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(_5255.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5258.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5263.BevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5268.ClutchConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5273.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(
                _5273.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5276.ConceptGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(
                _5276.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5279.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(
                _5279.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5284.CouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(
                _5284.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5286.CVTBeltConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(
                _5286.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CylindricalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(
                _5294.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5300.FaceGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5305.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5309.HypoidGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5313.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(
                _5313.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5316.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(
                _5316.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5319.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5327.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5336.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(
                _5336.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5339.RollingRingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5346.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5349.SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(
                _5349.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5352.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5355.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5364.TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5370.WormGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(_5370.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5373.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(
                _5373.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5181.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5181.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return (
            self._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
                self
            )
        )
