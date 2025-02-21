"""MountableComponentLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6813,
        _6819,
        _6822,
        _6825,
        _6826,
        _6827,
        _6833,
        _6839,
        _6841,
        _6844,
        _6850,
        _6852,
        _6856,
        _6861,
        _6866,
        _6884,
        _6890,
        _6905,
        _6912,
        _6915,
        _6918,
        _6921,
        _6922,
        _6926,
        _6930,
        _6935,
        _6938,
        _6939,
        _6940,
        _6943,
        _6947,
        _6949,
        _6953,
        _6957,
        _6959,
        _6962,
        _6965,
        _6966,
        _6967,
        _6969,
        _6970,
        _6974,
        _6975,
        _6980,
        _6981,
        _6982,
        _6985,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentLoadCase",)


Self = TypeVar("Self", bound="MountableComponentLoadCase")


class MountableComponentLoadCase(_6837.ComponentLoadCase):
    """MountableComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentLoadCase")

    class _Cast_MountableComponentLoadCase:
        """Special nested class for casting MountableComponentLoadCase to subclasses."""

        def __init__(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
            parent: "MountableComponentLoadCase",
        ):
            self._parent = parent

        @property
        def component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6837.ComponentLoadCase":
            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6813.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6819.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6822.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6825.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6826.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6827.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearLoadCase)

        @property
        def clutch_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6833.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6839.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6841.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6844.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6850.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6852.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6856.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.CVTPulleyLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6861.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6866.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6884.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.FaceGearLoadCase)

        @property
        def gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6890.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6905.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6912.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6915.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6921.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6922.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MeasurementComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6926.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6930.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6935.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(_6935.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6938.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6939.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6940.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6943.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6947.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6949.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.ShaftHubConnectionLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6953.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6957.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6959.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6962.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6965.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6966.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6967.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6969.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6970.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6974.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6975.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6980.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6981.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6982.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6985.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearLoadCase)

        @property
        def mountable_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "MountableComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentLoadCase.TYPE"):
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
    ) -> "MountableComponentLoadCase._Cast_MountableComponentLoadCase":
        return self._Cast_MountableComponentLoadCase(self)
