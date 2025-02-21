"""ConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3798
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3900,
        _3902,
        _3906,
        _3909,
        _3914,
        _3919,
        _3921,
        _3924,
        _3927,
        _3930,
        _3935,
        _3937,
        _3941,
        _3943,
        _3945,
        _3951,
        _3956,
        _3960,
        _3962,
        _3964,
        _3967,
        _3970,
        _3978,
        _3980,
        _3987,
        _3990,
        _3994,
        _3997,
        _4000,
        _4003,
        _4006,
        _4015,
        _4021,
        _4024,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundStabilityAnalysis")


class ConnectionCompoundStabilityAnalysis(_7539.ConnectionCompoundAnalysis):
    """ConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundStabilityAnalysis")

    class _Cast_ConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
            parent: "ConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3900.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(
                _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3906.BeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(_3906.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3909.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3914.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3919.ClutchConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3921.CoaxialConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3924.ConceptCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3927.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3930.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3935.CouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3937.CVTBeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3941.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(
                _3941.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3943.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(
                _3943.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3945.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3951.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3956.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3960.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3962.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3964.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3967.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3970.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3978.PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(
                _3978.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3980.PlanetaryConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(
                _3980.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3987.RingPinsToDiscConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3990.RollingRingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3994.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3997.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4000.SpringDamperConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4006.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4015.TorqueConverterConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4021.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4024.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "ConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3798.ConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectionStabilityAnalysis]

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
    ) -> "List[_3798.ConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectionStabilityAnalysis]

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
    ) -> (
        "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis"
    ):
        return self._Cast_ConnectionCompoundStabilityAnalysis(self)
