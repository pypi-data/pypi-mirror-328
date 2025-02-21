"""NamedDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility.databases import _1849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "NamedDatabase")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1847, _1842
    from mastapy.shafts import _25, _39
    from mastapy.nodal_analysis import _49
    from mastapy.materials import _249, _252, _271, _273, _275
    from mastapy.gears import _346
    from mastapy.gears.rating.cylindrical import _456, _472
    from mastapy.gears.materials import (
        _587,
        _589,
        _591,
        _592,
        _593,
        _595,
        _596,
        _598,
        _602,
        _603,
        _610,
    )
    from mastapy.gears.manufacturing.cylindrical import _613, _618, _629
    from mastapy.gears.manufacturing.cylindrical.cutters import _708, _714, _719, _720
    from mastapy.gears.manufacturing.bevel import _803
    from mastapy.gears.gear_set_pareto_optimiser import (
        _922,
        _924,
        _925,
        _927,
        _928,
        _929,
        _930,
        _931,
        _932,
        _933,
        _934,
        _935,
        _937,
        _938,
        _939,
        _940,
    )
    from mastapy.gears.gear_designs import _944, _946, _949
    from mastapy.gears.gear_designs.cylindrical import _1025, _1031
    from mastapy.electric_machines import _1302, _1320, _1333
    from mastapy.cycloidal import _1475, _1482
    from mastapy.bolts import _1485, _1487, _1489, _1494
    from mastapy.math_utility.optimisation import _1558, _1570
    from mastapy.bearings import _1900
    from mastapy.bearings.bearing_results.rolling import _1995
    from mastapy.system_model.optimization import _2248, _2256
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2584


__docformat__ = "restructuredtext en"
__all__ = ("NamedDatabase",)


Self = TypeVar("Self", bound="NamedDatabase")
TValue = TypeVar("TValue", bound="_1847.NamedDatabaseItem")


class NamedDatabase(_1849.SQLDatabase["_1848.NamedKey", TValue]):
    """NamedDatabase

    This is a mastapy class.

    Generic Types:
        TValue
    """

    TYPE = _NAMED_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedDatabase")

    class _Cast_NamedDatabase:
        """Special nested class for casting NamedDatabase to subclasses."""

        def __init__(
            self: "NamedDatabase._Cast_NamedDatabase", parent: "NamedDatabase"
        ):
            self._parent = parent

        @property
        def sql_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1849.SQLDatabase":
            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(self: "NamedDatabase._Cast_NamedDatabase") -> "_1842.Database":
            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def shaft_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_39.ShaftSettingsDatabase":
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_49.AnalysisSettingsDatabase":
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_249.BearingMaterialDatabase":
            from mastapy.materials import _249

            return self._parent._cast(_249.BearingMaterialDatabase)

        @property
        def component_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_252.ComponentMaterialDatabase":
            from mastapy.materials import _252

            return self._parent._cast(_252.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_271.LubricationDetailDatabase":
            from mastapy.materials import _271

            return self._parent._cast(_271.LubricationDetailDatabase)

        @property
        def material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_273.MaterialDatabase":
            from mastapy.materials import _273

            return self._parent._cast(_273.MaterialDatabase)

        @property
        def materials_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_275.MaterialsSettingsDatabase":
            from mastapy.materials import _275

            return self._parent._cast(_275.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_346.PocketingPowerLossCoefficientsDatabase":
            from mastapy.gears import _346

            return self._parent._cast(_346.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_456.CylindricalGearDesignAndRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _456

            return self._parent._cast(
                _456.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_472.CylindricalPlasticGearRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _472

            return self._parent._cast(_472.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_587.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _587

            return self._parent._cast(_587.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_589.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_591.BevelGearMaterialDatabase":
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_592.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_593.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_595.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_596.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_598.GearMaterialDatabase":
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_602.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
            from mastapy.gears.materials import _602

            return self._parent._cast(
                _602.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_603.KlingelnbergConicalGearMaterialDatabase":
            from mastapy.gears.materials import _603

            return self._parent._cast(_603.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_610.RawMaterialDatabase":
            from mastapy.gears.materials import _610

            return self._parent._cast(_610.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_613.CylindricalCutterDatabase":
            from mastapy.gears.manufacturing.cylindrical import _613

            return self._parent._cast(_613.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_618.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_629.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(_629.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_708.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _708

            return self._parent._cast(_708.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_714.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_719.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _719

            return self._parent._cast(_719.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_720.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_803.ManufacturingMachineDatabase":
            from mastapy.gears.manufacturing.bevel import _803

            return self._parent._cast(_803.ManufacturingMachineDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_922.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_927.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_929.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_930.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(
                _930.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_932.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_935.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(
                _938.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(
                _939.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_940.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _940

            return self._parent._cast(
                _940.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_944.BevelHypoidGearDesignSettingsDatabase":
            from mastapy.gears.gear_designs import _944

            return self._parent._cast(_944.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_946.BevelHypoidGearRatingSettingsDatabase":
            from mastapy.gears.gear_designs import _946

            return self._parent._cast(_946.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_949.DesignConstraintCollectionDatabase":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1025.CylindricalGearDesignConstraintsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1025

            return self._parent._cast(_1025.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1031.CylindricalGearMicroGeometrySettingsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1031

            return self._parent._cast(
                _1031.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1302.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1302

            return self._parent._cast(_1302.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1320.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1320

            return self._parent._cast(_1320.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1333.WindingMaterialDatabase":
            from mastapy.electric_machines import _1333

            return self._parent._cast(_1333.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1475.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1475

            return self._parent._cast(_1475.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1482.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1482

            return self._parent._cast(_1482.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1485.BoltedJointMaterialDatabase":
            from mastapy.bolts import _1485

            return self._parent._cast(_1485.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1487.BoltGeometryDatabase":
            from mastapy.bolts import _1487

            return self._parent._cast(_1487.BoltGeometryDatabase)

        @property
        def bolt_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1489.BoltMaterialDatabase":
            from mastapy.bolts import _1489

            return self._parent._cast(_1489.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1494.ClampedSectionMaterialDatabase":
            from mastapy.bolts import _1494

            return self._parent._cast(_1494.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1558.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1558

            return self._parent._cast(_1558.DesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1570.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1570

            return self._parent._cast(_1570.ParetoOptimisationStrategyDatabase)

        @property
        def bearing_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1900.BearingSettingsDatabase":
            from mastapy.bearings import _1900

            return self._parent._cast(_1900.BearingSettingsDatabase)

        @property
        def iso14179_settings_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_1995.ISO14179SettingsDatabase":
            from mastapy.bearings.bearing_results.rolling import _1995

            return self._parent._cast(_1995.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_2248.ConicalGearOptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2248

            return self._parent._cast(_2248.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_2256.OptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2256

            return self._parent._cast(_2256.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "_2584.SuperchargerRotorSetDatabase":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2584,
            )

            return self._parent._cast(_2584.SuperchargerRotorSetDatabase)

        @property
        def named_database(
            self: "NamedDatabase._Cast_NamedDatabase",
        ) -> "NamedDatabase":
            return self._parent

        def __getattr__(self: "NamedDatabase._Cast_NamedDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def create(self: Self, name: "str") -> "TValue":
        """TValue

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.Create(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate(
        self: Self, new_name: "str", item: "_1847.NamedDatabaseItem"
    ) -> "_1847.NamedDatabaseItem":
        """mastapy.utility.databases.NamedDatabaseItem

        Args:
            new_name (str)
            item (mastapy.utility.databases.NamedDatabaseItem)
        """
        new_name = str(new_name)
        method_result = self.wrapped.Duplicate(
            new_name if new_name else "", item.wrapped if item else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_value(self: Self, name: "str") -> "TValue":
        """TValue

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.GetValue(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def rename(self: Self, item: "_1847.NamedDatabaseItem", new_name: "str") -> "bool":
        """bool

        Args:
            item (mastapy.utility.databases.NamedDatabaseItem)
            new_name (str)
        """
        new_name = str(new_name)
        method_result = self.wrapped.Rename(
            item.wrapped if item else None, new_name if new_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "NamedDatabase._Cast_NamedDatabase":
        return self._Cast_NamedDatabase(self)
