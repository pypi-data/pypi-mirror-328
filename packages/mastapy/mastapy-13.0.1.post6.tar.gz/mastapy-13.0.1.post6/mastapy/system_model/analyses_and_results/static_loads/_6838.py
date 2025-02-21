"""ComponentLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6808,
        _6809,
        _6814,
        _6820,
        _6823,
        _6826,
        _6827,
        _6828,
        _6832,
        _6834,
        _6840,
        _6842,
        _6845,
        _6851,
        _6853,
        _6857,
        _6860,
        _6862,
        _6867,
        _6870,
        _6884,
        _6885,
        _6888,
        _6891,
        _6897,
        _6906,
        _6913,
        _6916,
        _6919,
        _6922,
        _6923,
        _6925,
        _6927,
        _6931,
        _6936,
        _6939,
        _6940,
        _6941,
        _6944,
        _6948,
        _6950,
        _6951,
        _6954,
        _6958,
        _6960,
        _6963,
        _6966,
        _6967,
        _6968,
        _6970,
        _6971,
        _6975,
        _6976,
        _6981,
        _6982,
        _6983,
        _6986,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentLoadCase",)


Self = TypeVar("Self", bound="ComponentLoadCase")


class ComponentLoadCase(_6929.PartLoadCase):
    """ComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentLoadCase")

    class _Cast_ComponentLoadCase:
        """Special nested class for casting ComponentLoadCase to subclasses."""

        def __init__(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
            parent: "ComponentLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6929.PartLoadCase":
            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6808.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6808

            return self._parent._cast(_6808.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6809.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(_6809.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6814.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6814

            return self._parent._cast(_6814.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6820.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6823.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6826.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6827.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6828.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelGearLoadCase)

        @property
        def bolt_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6832.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6834.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6840.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6842.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6845.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6851.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6853.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6857.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CVTPulleyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6860.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6862.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6867.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6870.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6884.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6885.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.FaceGearLoadCase)

        @property
        def fe_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6888.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FEPartLoadCase)

        @property
        def gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6891.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.GearLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6897.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6897

            return self._parent._cast(_6897.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6906.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6906

            return self._parent._cast(_6906.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6913.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6916.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(_6916.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6919.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(
                _6919.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6922.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6923.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(_6923.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6927.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6931.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6936.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6939.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6940.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(_6940.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6941.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6944.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6948.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6950.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6951.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.ShaftLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6954.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6958.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6960.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6963.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6966.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6967.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6968.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6970.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6971.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6975.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6976.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6981.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6982.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6983.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6986.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.ZerolBevelGearLoadCase)

        @property
        def component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "ComponentLoadCase":
            return self._parent

        def __getattr__(self: "ComponentLoadCase._Cast_ComponentLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def is_connected_to_ground(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsConnectedToGround

        if temp is None:
            return False

        return temp

    @property
    def is_torsionally_free(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTorsionallyFree

        if temp is None:
            return False

        return temp

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2444.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentLoadCase._Cast_ComponentLoadCase":
        return self._Cast_ComponentLoadCase(self)
