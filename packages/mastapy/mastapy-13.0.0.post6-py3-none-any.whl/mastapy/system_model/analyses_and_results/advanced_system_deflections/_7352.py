"""MountableComponentAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "MountableComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7276,
        _7280,
        _7283,
        _7286,
        _7287,
        _7288,
        _7295,
        _7300,
        _7301,
        _7304,
        _7308,
        _7312,
        _7315,
        _7320,
        _7324,
        _7327,
        _7332,
        _7336,
        _7340,
        _7343,
        _7346,
        _7350,
        _7351,
        _7353,
        _7357,
        _7360,
        _7361,
        _7362,
        _7363,
        _7364,
        _7366,
        _7371,
        _7374,
        _7379,
        _7380,
        _7383,
        _7386,
        _7387,
        _7389,
        _7390,
        _7391,
        _7394,
        _7395,
        _7397,
        _7398,
        _7399,
        _7402,
        _7354,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentAdvancedSystemDeflection")


class MountableComponentAdvancedSystemDeflection(
    _7297.ComponentAdvancedSystemDeflection
):
    """MountableComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentAdvancedSystemDeflection"
    )

    class _Cast_MountableComponentAdvancedSystemDeflection:
        """Special nested class for casting MountableComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
            parent: "MountableComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7297.ComponentAdvancedSystemDeflection":
            return self._parent._cast(_7297.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7354.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7276.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(
                _7276.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bearing_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7280.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(_7280.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7283.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(
                _7283.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7286.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(
                _7286.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7287.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7288.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(_7288.BevelGearAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7295.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7300.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7301.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7304.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7308.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7312.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7315.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.CVTPulleyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7320.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7324.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(
                _7324.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def face_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7327.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.FaceGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7332.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.GearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7336.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7340.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7343.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7346.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7350.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7351.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def oil_seal_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7353.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7357.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planet_carrier_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7360.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7361.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7362.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7363.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7364.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7366.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(_7366.RollingRingAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7371.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7374.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7379.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7380.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(
                _7380.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7383.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7386.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(
                _7386.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7387.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7389.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7390.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7391.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7394.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(_7394.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7395.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7397.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7398.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7399.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "_7402.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "MountableComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection":
        return self._Cast_MountableComponentAdvancedSystemDeflection(self)
