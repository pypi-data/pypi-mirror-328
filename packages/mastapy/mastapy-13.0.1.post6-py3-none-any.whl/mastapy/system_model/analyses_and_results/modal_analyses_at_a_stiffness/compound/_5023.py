"""ConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4892,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4991,
        _4993,
        _4997,
        _5000,
        _5005,
        _5010,
        _5012,
        _5015,
        _5018,
        _5021,
        _5026,
        _5028,
        _5032,
        _5034,
        _5036,
        _5042,
        _5047,
        _5051,
        _5053,
        _5055,
        _5058,
        _5061,
        _5069,
        _5071,
        _5078,
        _5081,
        _5085,
        _5088,
        _5091,
        _5094,
        _5097,
        _5106,
        _5112,
        _5115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConnectionCompoundModalAnalysisAtAStiffness")


class ConnectionCompoundModalAnalysisAtAStiffness(_7539.ConnectionCompoundAnalysis):
    """ConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
            parent: "ConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7539.ConnectionCompoundAnalysis":
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4993.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4993,
            )

            return self._parent._cast(
                _4993.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4997.BeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5000.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5010.ClutchConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5018.ConceptGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(
                _5026.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5028.CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5028,
            )

            return self._parent._cast(
                _5028.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(
                _5032.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(
                _5034.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5036.CylindricalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5042.FaceGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.HypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(
                _5069.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.PlanetaryConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(
                _5071.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5078.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5081.RollingRingConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5091.SpringDamperConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5106.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.WormGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5115.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "ConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConnectionCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4892.ConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4892.ConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConnectionModalAnalysisAtAStiffness]

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
    ) -> "ConnectionCompoundModalAnalysisAtAStiffness._Cast_ConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_ConnectionCompoundModalAnalysisAtAStiffness(self)
