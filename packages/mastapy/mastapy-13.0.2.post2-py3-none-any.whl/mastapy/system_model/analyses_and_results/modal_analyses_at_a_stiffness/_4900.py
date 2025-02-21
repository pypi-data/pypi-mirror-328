"""ConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4943,
        _4868,
        _4869,
        _4874,
        _4876,
        _4881,
        _4886,
        _4889,
        _4891,
        _4894,
        _4897,
        _4902,
        _4905,
        _4909,
        _4911,
        _4912,
        _4919,
        _4924,
        _4928,
        _4931,
        _4932,
        _4935,
        _4938,
        _4947,
        _4950,
        _4957,
        _4959,
        _4964,
        _4966,
        _4969,
        _4972,
        _4975,
        _4984,
        _4990,
        _4993,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConnectionModalAnalysisAtAStiffness")


class ConnectionModalAnalysisAtAStiffness(_7549.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionModalAnalysisAtAStiffness")

    class _Cast_ConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
            parent: "ConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4868.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4869.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4869,
            )

            return self._parent._cast(
                _4869.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4874.BeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4874,
            )

            return self._parent._cast(_4874.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4876.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(
                _4876.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4881.BevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4886.ClutchConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4889.CoaxialConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4891.ConceptCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(
                _4891.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4894.ConceptGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4897.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4902.CouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4905.CVTBeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(
                _4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(
                _4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4912.CylindricalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(
                _4912.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4919.FaceGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4924.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(_4924.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4928.HypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(_4928.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4931.InterMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(
                _4931.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4935.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(
                _4935.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4938.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(
                _4938.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4947.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(
                _4947.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4950.PlanetaryConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(
                _4950.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4957.RingPinsToDiscConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4959.RollingRingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(
                _4959.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4966.SpiralBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4969.SpringDamperConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(
                _4969.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4972.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4972,
            )

            return self._parent._cast(
                _4972.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4975.StraightBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(
                _4975.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4984.TorqueConverterConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(
                _4984.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4990.WormGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4990,
            )

            return self._parent._cast(_4990.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "_4993.ZerolBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4993,
            )

            return self._parent._cast(_4993.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
        ) -> "ConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_at_a_stiffness(self: Self) -> "_4943.ModalAnalysisAtAStiffness":
        """mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ModalAnalysisAtAStiffness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisAtAStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConnectionModalAnalysisAtAStiffness._Cast_ConnectionModalAnalysisAtAStiffness"
    ):
        return self._Cast_ConnectionModalAnalysisAtAStiffness(self)
