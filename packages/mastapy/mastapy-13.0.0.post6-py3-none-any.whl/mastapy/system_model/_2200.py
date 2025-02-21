"""Design"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List, Optional, Union, Tuple
from os import path


from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.class_property import classproperty
from mastapy._internal.implicit import (
    list_with_selected_item,
    enum_with_selected_value,
    overridable,
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials.efficiency import _292
from mastapy.system_model.part_model.gears import _2512
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2472, _2475
from mastapy._math.vector_3d import Vector3D
from mastapy.utility import _1581
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ARRAY = python_net_import("System", "Array")
_STRING = python_net_import("System", "String")
_BOOLEAN = python_net_import("System", "Boolean")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_DESIGN = python_net_import("SMT.MastaAPI.SystemModel", "Design")

if TYPE_CHECKING:
    from mastapy.system_model_gui import _1846
    from mastapy.gears import _322, _328
    from mastapy.system_model import _2223, _2224, _2208, _2205, _2222, _2212
    from mastapy.system_model.part_model import (
        _2478,
        _2474,
        _2468,
        _2433,
        _2434,
        _2435,
        _2436,
        _2439,
        _2442,
        _2443,
        _2444,
        _2447,
        _2448,
        _2452,
        _2453,
        _2454,
        _2455,
        _2462,
        _2463,
        _2464,
        _2466,
        _2469,
        _2471,
        _2476,
        _2477,
        _2479,
    )
    from mastapy.detailed_rigid_connectors.splines import _1390
    from mastapy.system_model.fe import _2361
    from mastapy.utility import _1582, _1583
    from mastapy.gears.materials import _598
    from mastapy.shafts import _35
    from mastapy.system_model.optimization.system_optimiser import _2240, _2239
    from mastapy.system_model.part_model.configurations import _2615, _2612, _2614
    from mastapy.bearings.bearing_results.rolling import _1976
    from mastapy.system_model.database_access import _2264
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5662,
        _5663,
        _5670,
    )
    from mastapy.system_model.part_model.gears import (
        _2533,
        _2513,
        _2514,
        _2515,
        _2516,
        _2517,
        _2518,
        _2519,
        _2520,
        _2521,
        _2522,
        _2523,
        _2524,
        _2525,
        _2526,
        _2527,
        _2528,
        _2529,
        _2530,
        _2532,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
        _2552,
        _2553,
        _2554,
    )
    from mastapy.system_model.analyses_and_results.static_loads import _6804, _6803
    from mastapy.utility.model_validation import _1793
    from mastapy.system_model.analyses_and_results.synchroniser_analysis import _2982
    from mastapy.system_model.part_model.creation_options import (
        _2571,
        _2572,
        _2573,
        _2574,
        _2575,
    )
    from mastapy.gears.gear_designs.creation_options import _1146, _1148, _1149
    from mastapy.nodal_analysis import _79
    from mastapy.bearings.bearing_designs.rolling import _2165
    from mastapy import _7558
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.part_model.cycloidal import _2568, _2569, _2570
    from mastapy.system_model.part_model.couplings import (
        _2576,
        _2578,
        _2579,
        _2581,
        _2582,
        _2583,
        _2584,
        _2586,
        _2587,
        _2588,
        _2589,
        _2590,
        _2596,
        _2597,
        _2598,
        _2600,
        _2601,
        _2602,
        _2604,
        _2605,
        _2606,
        _2607,
        _2608,
        _2610,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Design",)


Self = TypeVar("Self", bound="Design")


class Design(_0.APIBase):
    """Design

    This is a mastapy class.
    """

    TYPE = _DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Design")

    class _Cast_Design:
        """Special nested class for casting Design to subclasses."""

        def __init__(self: "Design._Cast_Design", parent: "Design"):
            self._parent = parent

        @property
        def design(self: "Design._Cast_Design") -> "Design":
            return self._parent

        def __getattr__(self: "Design._Cast_Design", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Design.TYPE" = None):
        super().__init__(instance_to_wrap if instance_to_wrap else Design.TYPE())
        self._freeze()

    @classproperty
    def available_examples(cls) -> "List[str]":
        """List[str]"""
        temp = Design.TYPE.AvailableExamples

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def masta_gui(self: Self) -> "_1846.MASTAGUI":
        """mastapy.system_model_gui.MASTAGUI

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MastaGUI

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def axial_contact_ratio_requirement(self: Self) -> "_322.ContactRatioRequirements":
        """mastapy.gears.ContactRatioRequirements"""
        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.ContactRatioRequirements"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._322", "ContactRatioRequirements"
        )(value)

    @axial_contact_ratio_requirement.setter
    @enforce_parameter_types
    def axial_contact_ratio_requirement(
        self: Self, value: "_322.ContactRatioRequirements"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.ContactRatioRequirements"
        )
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def bearing_configuration(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.BearingConfiguration

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @bearing_configuration.setter
    @enforce_parameter_types
    def bearing_configuration(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.BearingConfiguration = value

    @property
    def coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.CoefficientOfFriction = float(value) if value is not None else 0.0

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def default_save_location_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DefaultSaveLocationPath

        if temp is None:
            return ""

        return temp

    @property
    def design_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignName

        if temp is None:
            return ""

        return temp

    @design_name.setter
    @enforce_parameter_types
    def design_name(self: Self, value: "str"):
        self.wrapped.DesignName = str(value) if value is not None else ""

    @property
    def efficiency_rating_method_for_bearings(
        self: Self,
    ) -> "_292.BearingEfficiencyRatingMethod":
        """mastapy.materials.efficiency.BearingEfficiencyRatingMethod"""
        temp = self.wrapped.EfficiencyRatingMethodForBearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.BearingEfficiencyRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._292", "BearingEfficiencyRatingMethod"
        )(value)

    @efficiency_rating_method_for_bearings.setter
    @enforce_parameter_types
    def efficiency_rating_method_for_bearings(
        self: Self, value: "_292.BearingEfficiencyRatingMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.BearingEfficiencyRatingMethod"
        )
        self.wrapped.EfficiencyRatingMethodForBearings = value

    @property
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod":
        """EnumWithSelectedValue[mastapy.materials.efficiency.BearingEfficiencyRatingMethod]"""
        temp = self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @efficiency_rating_method_if_skf_loss_model_does_not_provide_losses.setter
    @enforce_parameter_types
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(
        self: Self, value: "_292.BearingEfficiencyRatingMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses = value

    @property
    def fe_substructure_configuration(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.FESubstructureConfiguration

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @fe_substructure_configuration.setter
    @enforce_parameter_types
    def fe_substructure_configuration(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.FESubstructureConfiguration = value

    @property
    def file_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FileName

        if temp is None:
            return ""

        return temp

    @property
    def gear_set_configuration(
        self: Self,
    ) -> (
        "list_with_selected_item.ListWithSelectedItem_ActiveGearSetDesignSelectionGroup"
    ):
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.ActiveGearSetDesignSelectionGroup]"""
        temp = self.wrapped.GearSetConfiguration

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ActiveGearSetDesignSelectionGroup",
        )(temp)

    @gear_set_configuration.setter
    @enforce_parameter_types
    def gear_set_configuration(
        self: Self, value: "_2512.ActiveGearSetDesignSelectionGroup"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ActiveGearSetDesignSelectionGroup.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ActiveGearSetDesignSelectionGroup.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.GearSetConfiguration = value

    @property
    def gravity_magnitude(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GravityMagnitude

        if temp is None:
            return 0.0

        return temp

    @gravity_magnitude.setter
    @enforce_parameter_types
    def gravity_magnitude(self: Self, value: "float"):
        self.wrapped.GravityMagnitude = float(value) if value is not None else 0.0

    @property
    def housing_material_for_grounded_connections(self: Self) -> "str":
        """str"""
        temp = self.wrapped.HousingMaterialForGroundedConnections.SelectedItemName

        if temp is None:
            return ""

        return temp

    @housing_material_for_grounded_connections.setter
    @enforce_parameter_types
    def housing_material_for_grounded_connections(self: Self, value: "str"):
        self.wrapped.HousingMaterialForGroundedConnections.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database.setter
    @enforce_parameter_types
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(
        self: Self, value: "str"
    ):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(
        self: Self,
    ) -> "str":
        """str"""
        temp = (
            self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SelectedItemName
        )

        if temp is None:
            return ""

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database.setter
    @enforce_parameter_types
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(
        self: Self, value: "str"
    ):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def input_power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.InputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @input_power_load.setter
    @enforce_parameter_types
    def input_power_load(self: Self, value: "_2472.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.InputPowerLoad = value

    @property
    def manufacturer(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Manufacturer

        if temp is None:
            return ""

        return temp

    @manufacturer.setter
    @enforce_parameter_types
    def manufacturer(self: Self, value: "str"):
        self.wrapped.Manufacturer = str(value) if value is not None else ""

    @property
    def maximum_acceptable_axial_contact_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_axial_contact_ratio(self: Self, value: "float"):
        self.wrapped.MaximumAcceptableAxialContactRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_acceptable_transverse_contact_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def maximum_acceptable_transverse_contact_ratio(self: Self, value: "float"):
        self.wrapped.MaximumAcceptableTransverseContactRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_number_of_teeth(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MaximumNumberOfTeeth

        if temp is None:
            return None

        return temp

    @maximum_number_of_teeth.setter
    @enforce_parameter_types
    def maximum_number_of_teeth(self: Self, value: "Optional[int]"):
        self.wrapped.MaximumNumberOfTeeth = value

    @property
    def maximum_number_of_teeth_external_gears(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MaximumNumberOfTeethExternalGears

        if temp is None:
            return None

        return temp

    @maximum_number_of_teeth_external_gears.setter
    @enforce_parameter_types
    def maximum_number_of_teeth_external_gears(self: Self, value: "Optional[int]"):
        self.wrapped.MaximumNumberOfTeethExternalGears = value

    @property
    def maximum_number_of_teeth_internal_gears(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MaximumNumberOfTeethInternalGears

        if temp is None:
            return None

        return temp

    @maximum_number_of_teeth_internal_gears.setter
    @enforce_parameter_types
    def maximum_number_of_teeth_internal_gears(self: Self, value: "Optional[int]"):
        self.wrapped.MaximumNumberOfTeethInternalGears = value

    @property
    def minimum_acceptable_axial_contact_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_axial_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_axial_contact_ratio(self: Self, value: "float"):
        self.wrapped.MinimumAcceptableAxialContactRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_acceptable_transverse_contact_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def minimum_acceptable_transverse_contact_ratio(self: Self, value: "float"):
        self.wrapped.MinimumAcceptableTransverseContactRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_number_of_teeth(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MinimumNumberOfTeeth

        if temp is None:
            return None

        return temp

    @minimum_number_of_teeth.setter
    @enforce_parameter_types
    def minimum_number_of_teeth(self: Self, value: "Optional[int]"):
        self.wrapped.MinimumNumberOfTeeth = value

    @property
    def minimum_number_of_teeth_external_gears(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MinimumNumberOfTeethExternalGears

        if temp is None:
            return None

        return temp

    @minimum_number_of_teeth_external_gears.setter
    @enforce_parameter_types
    def minimum_number_of_teeth_external_gears(self: Self, value: "Optional[int]"):
        self.wrapped.MinimumNumberOfTeethExternalGears = value

    @property
    def minimum_number_of_teeth_internal_gears(self: Self) -> "Optional[int]":
        """Optional[int]"""
        temp = self.wrapped.MinimumNumberOfTeethInternalGears

        if temp is None:
            return None

        return temp

    @minimum_number_of_teeth_internal_gears.setter
    @enforce_parameter_types
    def minimum_number_of_teeth_internal_gears(self: Self, value: "Optional[int]"):
        self.wrapped.MinimumNumberOfTeethInternalGears = value

    @property
    def node_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NodeSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @node_size.setter
    @enforce_parameter_types
    def node_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NodeSize = value

    @property
    def number_of_gear_set_configurations(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfGearSetConfigurations

        if temp is None:
            return 0

        return temp

    @property
    def output_power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.OutputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @output_power_load.setter
    @enforce_parameter_types
    def output_power_load(self: Self, value: "_2472.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.OutputPowerLoad = value

    @property
    def save_external_fe_files_in_the_default_subfolder(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SaveExternalFEFilesInTheDefaultSubfolder

        if temp is None:
            return False

        return temp

    @save_external_fe_files_in_the_default_subfolder.setter
    @enforce_parameter_types
    def save_external_fe_files_in_the_default_subfolder(self: Self, value: "bool"):
        self.wrapped.SaveExternalFEFilesInTheDefaultSubfolder = (
            bool(value) if value is not None else False
        )

    @property
    def shaft_detail_configuration(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ShaftDetailConfiguration

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @shaft_detail_configuration.setter
    @enforce_parameter_types
    def shaft_detail_configuration(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ShaftDetailConfiguration = value

    @property
    def shaft_diameter_modification_due_to_rolling_bearing_rings(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing":
        """EnumWithSelectedValue[mastapy.system_model.part_model.ShaftDiameterModificationDueToRollingBearingRing]"""
        temp = self.wrapped.ShaftDiameterModificationDueToRollingBearingRings

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @shaft_diameter_modification_due_to_rolling_bearing_rings.setter
    @enforce_parameter_types
    def shaft_diameter_modification_due_to_rolling_bearing_rings(
        self: Self, value: "_2475.ShaftDiameterModificationDueToRollingBearingRing"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftDiameterModificationDueToRollingBearingRings = value

    @property
    def thermal_expansion_for_grounded_nodes(
        self: Self,
    ) -> "_2223.ThermalExpansionOptionForGroundedNodes":
        """mastapy.system_model.ThermalExpansionOptionForGroundedNodes"""
        temp = self.wrapped.ThermalExpansionForGroundedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.ThermalExpansionOptionForGroundedNodes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2223", "ThermalExpansionOptionForGroundedNodes"
        )(value)

    @thermal_expansion_for_grounded_nodes.setter
    @enforce_parameter_types
    def thermal_expansion_for_grounded_nodes(
        self: Self, value: "_2223.ThermalExpansionOptionForGroundedNodes"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.ThermalExpansionOptionForGroundedNodes"
        )
        self.wrapped.ThermalExpansionForGroundedNodes = value

    @property
    def transverse_contact_ratio_requirement(
        self: Self,
    ) -> "_322.ContactRatioRequirements":
        """mastapy.gears.ContactRatioRequirements"""
        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.ContactRatioRequirements"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._322", "ContactRatioRequirements"
        )(value)

    @transverse_contact_ratio_requirement.setter
    @enforce_parameter_types
    def transverse_contact_ratio_requirement(
        self: Self, value: "_322.ContactRatioRequirements"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.ContactRatioRequirements"
        )
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def unbalanced_mass_inclusion(self: Self) -> "_2478.UnbalancedMassInclusionOption":
        """mastapy.system_model.part_model.UnbalancedMassInclusionOption"""
        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.UnbalancedMassInclusionOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model._2478", "UnbalancedMassInclusionOption"
        )(value)

    @unbalanced_mass_inclusion.setter
    @enforce_parameter_types
    def unbalanced_mass_inclusion(
        self: Self, value: "_2478.UnbalancedMassInclusionOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.UnbalancedMassInclusionOption"
        )
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings

        if temp is None:
            return False

        return temp

    @use_element_contact_angles_for_angular_velocities_in_ball_bearings.setter
    @enforce_parameter_types
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(
        self: Self, value: "bool"
    ):
        self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings = (
            bool(value) if value is not None else False
        )

    @property
    def use_expanded_2d_projection_mode(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseExpanded2DProjectionMode

        if temp is None:
            return False

        return temp

    @use_expanded_2d_projection_mode.setter
    @enforce_parameter_types
    def use_expanded_2d_projection_mode(self: Self, value: "bool"):
        self.wrapped.UseExpanded2DProjectionMode = (
            bool(value) if value is not None else False
        )

    @property
    def volumetric_oil_air_mixture_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VolumetricOilAirMixtureRatio

        if temp is None:
            return 0.0

        return temp

    @volumetric_oil_air_mixture_ratio.setter
    @enforce_parameter_types
    def volumetric_oil_air_mixture_ratio(self: Self, value: "float"):
        self.wrapped.VolumetricOilAirMixtureRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def default_system_temperatures(self: Self) -> "_2224.TransmissionTemperatureSet":
        """mastapy.system_model.TransmissionTemperatureSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DefaultSystemTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def detailed_spline_settings(self: Self) -> "_1390.DetailedSplineJointSettings":
        """mastapy.detailed_rigid_connectors.splines.DetailedSplineJointSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DetailedSplineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def electric_machine_group(self: Self) -> "_2208.ElectricMachineGroup":
        """mastapy.system_model.ElectricMachineGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def fe_batch_operations(self: Self) -> "_2361.BatchOperations":
        """mastapy.system_model.fe.BatchOperations

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEBatchOperations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def file_save_details_all(self: Self) -> "_1582.FileHistory":
        """mastapy.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FileSaveDetailsAll

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def file_save_details_most_recent(self: Self) -> "_1583.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FileSaveDetailsMostRecent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_design_group(self: Self) -> "_328.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gravity_orientation(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.GravityOrientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @gravity_orientation.setter
    @enforce_parameter_types
    def gravity_orientation(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityOrientation = value

    @property
    def gravity_vector_components(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.GravityVectorComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @gravity_vector_components.setter
    @enforce_parameter_types
    def gravity_vector_components(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityVectorComponents = value

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_external_external_meshes(
        self: Self,
    ) -> "_598.ISOTR1417912001CoefficientOfFrictionConstants":
        """mastapy.gears.materials.ISOTR1417912001CoefficientOfFrictionConstants

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes(
        self: Self,
    ) -> "_598.ISOTR1417912001CoefficientOfFrictionConstants":
        """mastapy.gears.materials.ISOTR1417912001CoefficientOfFrictionConstants

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_gear_set_selection_group(
        self: Self,
    ) -> "_2512.ActiveGearSetDesignSelectionGroup":
        """mastapy.system_model.part_model.gears.ActiveGearSetDesignSelectionGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedGearSetSelectionGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def settings(self: Self) -> "_2205.DesignSettings":
        """mastapy.system_model.DesignSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shafts(self: Self) -> "_35.ShaftSafetyFactorSettings":
        """mastapy.shafts.ShaftSafetyFactorSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shafts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system(self: Self) -> "_2222.SystemReporting":
        """mastapy.system_model.SystemReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.System

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_optimiser_details(self: Self) -> "_2240.SystemOptimiserDetails":
        """mastapy.system_model.optimization.system_optimiser.SystemOptimiserDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemOptimiserDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_detail_configurations(
        self: Self,
    ) -> "List[_2615.BearingDetailConfiguration]":
        """List[mastapy.system_model.part_model.configurations.BearingDetailConfiguration]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_substructure_configurations(
        self: Self,
    ) -> "List[_2612.ActiveFESubstructureSelectionGroup]":
        """List[mastapy.system_model.part_model.configurations.ActiveFESubstructureSelectionGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructureConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_configurations(
        self: Self,
    ) -> "List[_2512.ActiveGearSetDesignSelectionGroup]":
        """List[mastapy.system_model.part_model.gears.ActiveGearSetDesignSelectionGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def iso14179_settings_per_bearing_type(
        self: Self,
    ) -> "List[_1976.ISO14179SettingsPerBearingType]":
        """List[mastapy.bearings.bearing_results.rolling.ISO14179SettingsPerBearingType]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179SettingsPerBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_detail_configurations(
        self: Self,
    ) -> "List[_2614.ActiveShaftDesignSelectionGroup]":
        """List[mastapy.system_model.part_model.configurations.ActiveShaftDesignSelectionGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def databases(self: Self) -> "_2264.Databases":
        """mastapy.system_model.database_access.Databases

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Databases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_states(self: Self) -> "List[_5662.DesignState]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def duty_cycles(self: Self) -> "List[_5663.DutyCycle]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_config(self: Self) -> "_2533.GearSetConfiguration":
        """mastapy.system_model.part_model.gears.GearSetConfiguration"""
        temp = self.wrapped.GearSetConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @gear_set_config.setter
    @enforce_parameter_types
    def gear_set_config(self: Self, value: "_2533.GearSetConfiguration"):
        self.wrapped.GearSetConfig = value.wrapped

    @property
    def masta_settings(self: Self) -> "_2212.MASTASettings":
        """mastapy.system_model.MASTASettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MastaSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_assembly(self: Self) -> "_2474.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_loads(self: Self) -> "List[_6804.StaticLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1793.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_optimiser(self: Self) -> "_2239.SystemOptimiser":
        """mastapy.system_model.optimization.system_optimiser.SystemOptimiser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemOptimiser

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case_groups(
        self: Self,
    ) -> "List[_5670.TimeSeriesLoadCaseGroup]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCaseGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def add_design_state(
        self: Self, name: "str" = "New Design State"
    ) -> "_5662.DesignState":
        """mastapy.system_model.analyses_and_results.load_case_groups.DesignState

        Args:
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.AddDesignState(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_duty_cycle(self: Self, name: "str" = "New Duty Cycle") -> "_5663.DutyCycle":
        """mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle

        Args:
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.AddDutyCycle(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def add_synchroniser_shift_empty(self: Self) -> "_2982.SynchroniserShift":
        """mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift"""
        method_result = self.wrapped.AddSynchroniserShift()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_synchroniser_shift(self: Self, name: "str") -> "_2982.SynchroniserShift":
        """mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.AddSynchroniserShift.Overloads[_STRING](
            name if name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def clear_design(self: Self):
        """Method does not return."""
        self.wrapped.ClearDesign()

    def __copy__(self: Self) -> "Design":
        """mastapy.system_model.Design"""
        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def __deepcopy__(self: Self, memo) -> "Design":
        """mastapy.system_model.Design"""
        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def copy_with_results(self: Self) -> "Design":
        """mastapy.system_model.Design"""
        method_result = self.wrapped.CopyWithResults()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def design_state_load_case_group_named(
        self: Self, name: "str"
    ) -> "_5662.DesignState":
        """mastapy.system_model.analyses_and_results.load_case_groups.DesignState

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.DesignStateLoadCaseGroupNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def design_state_named(self: Self, name: "str") -> "_5662.DesignState":
        """mastapy.system_model.analyses_and_results.load_case_groups.DesignState

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.DesignStateNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def duty_cycle_named(self: Self, name: "str") -> "_5663.DutyCycle":
        """mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.DutyCycleNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def load_results(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.LoadResults(file_name if file_name else "")

    @enforce_parameter_types
    def new_belt_creation_options(
        self: Self,
        centre_distance: "float" = 0.1,
        pulley_a_diameter: "float" = 0.08,
        pulley_b_diameter: "float" = 0.08,
        name: "str" = "Belt Drive",
    ) -> "_2571.BeltCreationOptions":
        """mastapy.system_model.part_model.creation_options.BeltCreationOptions

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)
        """
        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.NewBeltCreationOptions(
            centre_distance if centre_distance else 0.0,
            pulley_a_diameter if pulley_a_diameter else 0.0,
            pulley_b_diameter if pulley_b_diameter else 0.0,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def new_cycloidal_assembly_creation_options(
        self: Self,
        number_of_discs: "int" = 1,
        number_of_pins: "int" = 10,
        name: "str" = "Cycloidal Assembly",
    ) -> "_2572.CycloidalAssemblyCreationOptions":
        """mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)
        """
        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.NewCycloidalAssemblyCreationOptions(
            number_of_discs if number_of_discs else 0,
            number_of_pins if number_of_pins else 0,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def new_cylindrical_gear_linear_train_creation_options(
        self: Self, number_of_gears: "int" = 3, name: "str" = "Gear Train"
    ) -> "_2573.CylindricalGearLinearTrainCreationOptions":
        """mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions

        Args:
            number_of_gears (int, optional)
            name (str, optional)
        """
        number_of_gears = int(number_of_gears)
        name = str(name)
        method_result = self.wrapped.NewCylindricalGearLinearTrainCreationOptions(
            number_of_gears if number_of_gears else 0, name if name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def new_cylindrical_gear_pair_creation_options(
        self: Self,
    ) -> "_1146.CylindricalGearPairCreationOptions":
        """mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions"""
        method_result = self.wrapped.NewCylindricalGearPairCreationOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def new_hypoid_gear_set_creation_options(
        self: Self,
    ) -> "_1148.HypoidGearSetCreationOptions":
        """mastapy.gears.gear_designs.creation_options.HypoidGearSetCreationOptions"""
        method_result = self.wrapped.NewHypoidGearSetCreationOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def new_nodal_matrix(
        self: Self, dense_matrix: "List[List[float]]"
    ) -> "_79.NodalMatrix":
        """mastapy.nodal_analysis.NodalMatrix

        Args:
            dense_matrix (List[List[float]])
        """
        dense_matrix = conversion.mp_to_pn_list_float_2d(dense_matrix)
        method_result = self.wrapped.NewNodalMatrix(dense_matrix)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def new_planet_carrier_creation_options(
        self: Self, number_of_planets: "int" = 3, diameter: "float" = 0.05
    ) -> "_2574.PlanetCarrierCreationOptions":
        """mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)
        """
        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.NewPlanetCarrierCreationOptions(
            number_of_planets if number_of_planets else 0, diameter if diameter else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def new_shaft_creation_options(
        self: Self,
        length: "float" = 0.1,
        outer_diameter: "float" = 0.025,
        bore: "float" = 0.0,
        name: "str" = "Shaft",
    ) -> "_2575.ShaftCreationOptions":
        """mastapy.system_model.part_model.creation_options.ShaftCreationOptions

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)
        """
        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.NewShaftCreationOptions(
            length if length else 0.0,
            outer_diameter if outer_diameter else 0.0,
            bore if bore else 0.0,
            name if name else "",
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def new_spiral_bevel_gear_set_creation_options(
        self: Self,
    ) -> "_1149.SpiralBevelGearSetCreationOptions":
        """mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions"""
        method_result = self.wrapped.NewSpiralBevelGearSetCreationOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_bearing_from_database(
        self: Self, rolling_bearing: "_2165.RollingBearing"
    ):
        """Method does not return.

        Args:
            rolling_bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """
        self.wrapped.RemoveBearingFromDatabase(
            rolling_bearing.wrapped if rolling_bearing else None
        )

    @enforce_parameter_types
    def remove_synchroniser_shift(self: Self, shift: "_2982.SynchroniserShift"):
        """Method does not return.

        Args:
            shift (mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift)
        """
        self.wrapped.RemoveSynchroniserShift(shift.wrapped if shift else None)

    @enforce_parameter_types
    def save(self: Self, file_name: "str", save_results: "bool") -> "_1793.Status":
        """mastapy.utility.model_validation.Status

        Args:
            file_name (str)
            save_results (bool)
        """
        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN](
            file_name if file_name else "", save_results if save_results else False
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def save_with_progress(
        self: Self,
        file_name: "str",
        save_results: "bool",
        progress: "_7558.TaskProgress",
    ) -> "_1793.Status":
        """mastapy.utility.model_validation.Status

        Args:
            file_name (str)
            save_results (bool)
            progress (mastapy.TaskProgress)
        """
        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN, _TASK_PROGRESS](
            file_name if file_name else "",
            save_results if save_results else False,
            progress.wrapped if progress else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def save_load_case_results(
        self: Self, file_name: "str", load_cases: "List[_6803.LoadCase]"
    ):
        """Method does not return.

        Args:
            file_name (str)
            load_cases (List[mastapy.system_model.analyses_and_results.static_loads.LoadCase])
        """
        file_name = str(file_name)
        load_cases = conversion.mp_to_pn_objects_in_dotnet_list(load_cases)
        self.wrapped.SaveLoadCaseResults(file_name if file_name else "", load_cases)

    @enforce_parameter_types
    def save_results(self: Self, file_name: "str"):
        """Method does not return.

        Args:
            file_name (str)
        """
        file_name = str(file_name)
        self.wrapped.SaveResults(file_name if file_name else "")

    @enforce_parameter_types
    def time_series_load_case_group_named(
        self: Self, name: "str"
    ) -> "_5670.TimeSeriesLoadCaseGroup":
        """mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.TimeSeriesLoadCaseGroupNamed(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def all_parts(self: Self) -> "List[_2468.Part]":
        """List[mastapy.system_model.part_model.Part]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_assembly(self: Self) -> "List[_2433.Assembly]":
        """List[mastapy.system_model.part_model.Assembly]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_assembly(
        self: Self,
    ) -> "List[_2434.AbstractAssembly]":
        """List[mastapy.system_model.part_model.AbstractAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_shaft(self: Self) -> "List[_2435.AbstractShaft]":
        """List[mastapy.system_model.part_model.AbstractShaft]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_shaft_or_housing(
        self: Self,
    ) -> "List[_2436.AbstractShaftOrHousing]":
        """List[mastapy.system_model.part_model.AbstractShaftOrHousing]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bearing(self: Self) -> "List[_2439.Bearing]":
        """List[mastapy.system_model.part_model.Bearing]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bolt(self: Self) -> "List[_2442.Bolt]":
        """List[mastapy.system_model.part_model.Bolt]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bolted_joint(self: Self) -> "List[_2443.BoltedJoint]":
        """List[mastapy.system_model.part_model.BoltedJoint]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_component(self: Self) -> "List[_2444.Component]":
        """List[mastapy.system_model.part_model.Component]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_connector(self: Self) -> "List[_2447.Connector]":
        """List[mastapy.system_model.part_model.Connector]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_datum(self: Self) -> "List[_2448.Datum]":
        """List[mastapy.system_model.part_model.Datum]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_external_cad_model(
        self: Self,
    ) -> "List[_2452.ExternalCADModel]":
        """List[mastapy.system_model.part_model.ExternalCADModel]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_fe_part(self: Self) -> "List[_2453.FEPart]":
        """List[mastapy.system_model.part_model.FEPart]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_flexible_pin_assembly(
        self: Self,
    ) -> "List[_2454.FlexiblePinAssembly]":
        """List[mastapy.system_model.part_model.FlexiblePinAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_guide_dxf_model(self: Self) -> "List[_2455.GuideDxfModel]":
        """List[mastapy.system_model.part_model.GuideDxfModel]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_mass_disc(self: Self) -> "List[_2462.MassDisc]":
        """List[mastapy.system_model.part_model.MassDisc]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_measurement_component(
        self: Self,
    ) -> "List[_2463.MeasurementComponent]":
        """List[mastapy.system_model.part_model.MeasurementComponent]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_mountable_component(
        self: Self,
    ) -> "List[_2464.MountableComponent]":
        """List[mastapy.system_model.part_model.MountableComponent]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_oil_seal(self: Self) -> "List[_2466.OilSeal]":
        """List[mastapy.system_model.part_model.OilSeal]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_planet_carrier(self: Self) -> "List[_2469.PlanetCarrier]":
        """List[mastapy.system_model.part_model.PlanetCarrier]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_point_load(self: Self) -> "List[_2471.PointLoad]":
        """List[mastapy.system_model.part_model.PointLoad]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_power_load(self: Self) -> "List[_2472.PowerLoad]":
        """List[mastapy.system_model.part_model.PowerLoad]"""
        cast_type = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_root_assembly(self: Self) -> "List[_2474.RootAssembly]":
        """List[mastapy.system_model.part_model.RootAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "RootAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_specialised_assembly(
        self: Self,
    ) -> "List[_2476.SpecialisedAssembly]":
        """List[mastapy.system_model.part_model.SpecialisedAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_unbalanced_mass(self: Self) -> "List[_2477.UnbalancedMass]":
        """List[mastapy.system_model.part_model.UnbalancedMass]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_virtual_component(
        self: Self,
    ) -> "List[_2479.VirtualComponent]":
        """List[mastapy.system_model.part_model.VirtualComponent]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_shaft(self: Self) -> "List[_2482.Shaft]":
        """List[mastapy.system_model.part_model.shaft_model.Shaft]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_agma_gleason_conical_gear(
        self: Self,
    ) -> "List[_2513.AGMAGleasonConicalGear]":
        """List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_agma_gleason_conical_gear_set(
        self: Self,
    ) -> "List[_2514.AGMAGleasonConicalGearSet]":
        """List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_gear(
        self: Self,
    ) -> "List[_2515.BevelDifferentialGear]":
        """List[mastapy.system_model.part_model.gears.BevelDifferentialGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_gear_set(
        self: Self,
    ) -> "List[_2516.BevelDifferentialGearSet]":
        """List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_planet_gear(
        self: Self,
    ) -> "List[_2517.BevelDifferentialPlanetGear]":
        """List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_sun_gear(
        self: Self,
    ) -> "List[_2518.BevelDifferentialSunGear]":
        """List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_gear(self: Self) -> "List[_2519.BevelGear]":
        """List[mastapy.system_model.part_model.gears.BevelGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_gear_set(self: Self) -> "List[_2520.BevelGearSet]":
        """List[mastapy.system_model.part_model.gears.BevelGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_gear(self: Self) -> "List[_2521.ConceptGear]":
        """List[mastapy.system_model.part_model.gears.ConceptGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_gear_set(self: Self) -> "List[_2522.ConceptGearSet]":
        """List[mastapy.system_model.part_model.gears.ConceptGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_conical_gear(self: Self) -> "List[_2523.ConicalGear]":
        """List[mastapy.system_model.part_model.gears.ConicalGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_conical_gear_set(self: Self) -> "List[_2524.ConicalGearSet]":
        """List[mastapy.system_model.part_model.gears.ConicalGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_gear(self: Self) -> "List[_2525.CylindricalGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_gear_set(
        self: Self,
    ) -> "List[_2526.CylindricalGearSet]":
        """List[mastapy.system_model.part_model.gears.CylindricalGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_planet_gear(
        self: Self,
    ) -> "List[_2527.CylindricalPlanetGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_face_gear(self: Self) -> "List[_2528.FaceGear]":
        """List[mastapy.system_model.part_model.gears.FaceGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_face_gear_set(self: Self) -> "List[_2529.FaceGearSet]":
        """List[mastapy.system_model.part_model.gears.FaceGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_gear(self: Self) -> "List[_2530.Gear]":
        """List[mastapy.system_model.part_model.gears.Gear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_gear_set(self: Self) -> "List[_2532.GearSet]":
        """List[mastapy.system_model.part_model.gears.GearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_hypoid_gear(self: Self) -> "List[_2534.HypoidGear]":
        """List[mastapy.system_model.part_model.gears.HypoidGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_hypoid_gear_set(self: Self) -> "List[_2535.HypoidGearSet]":
        """List[mastapy.system_model.part_model.gears.HypoidGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(
        self: Self,
    ) -> "List[_2536.KlingelnbergCycloPalloidConicalGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidConicalGear",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self,
    ) -> "List[_2537.KlingelnbergCycloPalloidConicalGearSet]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidConicalGearSet",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self,
    ) -> "List[_2538.KlingelnbergCycloPalloidHypoidGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidHypoidGear",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self,
    ) -> "List[_2539.KlingelnbergCycloPalloidHypoidGearSet]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidHypoidGearSet",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self,
    ) -> "List[_2540.KlingelnbergCycloPalloidSpiralBevelGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidSpiralBevelGear",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self,
    ) -> "List[_2541.KlingelnbergCycloPalloidSpiralBevelGearSet]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears",
            "KlingelnbergCycloPalloidSpiralBevelGearSet",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_planetary_gear_set(
        self: Self,
    ) -> "List[_2542.PlanetaryGearSet]":
        """List[mastapy.system_model.part_model.gears.PlanetaryGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spiral_bevel_gear(
        self: Self,
    ) -> "List[_2543.SpiralBevelGear]":
        """List[mastapy.system_model.part_model.gears.SpiralBevelGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spiral_bevel_gear_set(
        self: Self,
    ) -> "List[_2544.SpiralBevelGearSet]":
        """List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_diff_gear(
        self: Self,
    ) -> "List[_2545.StraightBevelDiffGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_diff_gear_set(
        self: Self,
    ) -> "List[_2546.StraightBevelDiffGearSet]":
        """List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_gear(
        self: Self,
    ) -> "List[_2547.StraightBevelGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_gear_set(
        self: Self,
    ) -> "List[_2548.StraightBevelGearSet]":
        """List[mastapy.system_model.part_model.gears.StraightBevelGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_planet_gear(
        self: Self,
    ) -> "List[_2549.StraightBevelPlanetGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_sun_gear(
        self: Self,
    ) -> "List[_2550.StraightBevelSunGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelSunGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_worm_gear(self: Self) -> "List[_2551.WormGear]":
        """List[mastapy.system_model.part_model.gears.WormGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_worm_gear_set(self: Self) -> "List[_2552.WormGearSet]":
        """List[mastapy.system_model.part_model.gears.WormGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_zerol_bevel_gear(self: Self) -> "List[_2553.ZerolBevelGear]":
        """List[mastapy.system_model.part_model.gears.ZerolBevelGear]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_zerol_bevel_gear_set(
        self: Self,
    ) -> "List[_2554.ZerolBevelGearSet]":
        """List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cycloidal_assembly(
        self: Self,
    ) -> "List[_2568.CycloidalAssembly]":
        """List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cycloidal_disc(self: Self) -> "List[_2569.CycloidalDisc]":
        """List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_ring_pins(self: Self) -> "List[_2570.RingPins]":
        """List[mastapy.system_model.part_model.cycloidal.RingPins]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_belt_drive(self: Self) -> "List[_2576.BeltDrive]":
        """List[mastapy.system_model.part_model.couplings.BeltDrive]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_clutch(self: Self) -> "List[_2578.Clutch]":
        """List[mastapy.system_model.part_model.couplings.Clutch]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_clutch_half(self: Self) -> "List[_2579.ClutchHalf]":
        """List[mastapy.system_model.part_model.couplings.ClutchHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_coupling(self: Self) -> "List[_2581.ConceptCoupling]":
        """List[mastapy.system_model.part_model.couplings.ConceptCoupling]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_coupling_half(
        self: Self,
    ) -> "List[_2582.ConceptCouplingHalf]":
        """List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_coupling(self: Self) -> "List[_2583.Coupling]":
        """List[mastapy.system_model.part_model.couplings.Coupling]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_coupling_half(self: Self) -> "List[_2584.CouplingHalf]":
        """List[mastapy.system_model.part_model.couplings.CouplingHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cvt(self: Self) -> "List[_2586.CVT]":
        """List[mastapy.system_model.part_model.couplings.CVT]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cvt_pulley(self: Self) -> "List[_2587.CVTPulley]":
        """List[mastapy.system_model.part_model.couplings.CVTPulley]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_part_to_part_shear_coupling(
        self: Self,
    ) -> "List[_2588.PartToPartShearCoupling]":
        """List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_part_to_part_shear_coupling_half(
        self: Self,
    ) -> "List[_2589.PartToPartShearCouplingHalf]":
        """List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings",
            "PartToPartShearCouplingHalf",
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_pulley(self: Self) -> "List[_2590.Pulley]":
        """List[mastapy.system_model.part_model.couplings.Pulley]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_rolling_ring(self: Self) -> "List[_2596.RollingRing]":
        """List[mastapy.system_model.part_model.couplings.RollingRing]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_rolling_ring_assembly(
        self: Self,
    ) -> "List[_2597.RollingRingAssembly]":
        """List[mastapy.system_model.part_model.couplings.RollingRingAssembly]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_shaft_hub_connection(
        self: Self,
    ) -> "List[_2598.ShaftHubConnection]":
        """List[mastapy.system_model.part_model.couplings.ShaftHubConnection]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spring_damper(self: Self) -> "List[_2600.SpringDamper]":
        """List[mastapy.system_model.part_model.couplings.SpringDamper]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spring_damper_half(
        self: Self,
    ) -> "List[_2601.SpringDamperHalf]":
        """List[mastapy.system_model.part_model.couplings.SpringDamperHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser(self: Self) -> "List[_2602.Synchroniser]":
        """List[mastapy.system_model.part_model.couplings.Synchroniser]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_half(
        self: Self,
    ) -> "List[_2604.SynchroniserHalf]":
        """List[mastapy.system_model.part_model.couplings.SynchroniserHalf]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_part(
        self: Self,
    ) -> "List[_2605.SynchroniserPart]":
        """List[mastapy.system_model.part_model.couplings.SynchroniserPart]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_sleeve(
        self: Self,
    ) -> "List[_2606.SynchroniserSleeve]":
        """List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter(self: Self) -> "List[_2607.TorqueConverter]":
        """List[mastapy.system_model.part_model.couplings.TorqueConverter]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter_pump(
        self: Self,
    ) -> "List[_2608.TorqueConverterPump]":
        """List[mastapy.system_model.part_model.couplings.TorqueConverterPump]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter_turbine(
        self: Self,
    ) -> "List[_2610.TorqueConverterTurbine]":
        """List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]"""
        cast_type = python_net_import(
            "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
        )
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    @staticmethod
    @enforce_parameter_types
    def load(
        file_path: "str",
        load_full_fe_option: "_1581.ExternalFullFEFileOption" = _1581.ExternalFullFEFileOption.MESH_AND_EXPANSION_VECTORS,
    ) -> "Design":
        """mastapy.system_model.Design

        Args:
            file_path (str)
            load_full_fe_option (mastapy.utility.ExternalFullFEFileOption, optional)
        """
        file_path = str(file_path)
        file_path = path.abspath(file_path)
        load_full_fe_option = conversion.mp_to_pn_enum(
            load_full_fe_option, "SMT.MastaAPI.Utility.ExternalFullFEFileOption"
        )
        method_result = Design.TYPE.Load(
            file_path if file_path else "", load_full_fe_option
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @staticmethod
    @enforce_parameter_types
    def load_example(example_string: "str") -> "Design":
        """mastapy.system_model.Design

        Args:
            example_string (str)
        """
        example_string = str(example_string)
        method_result = Design.TYPE.LoadExample(
            example_string if example_string else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def compare_for_test_only(self: Self, design: "Design", sb: "str") -> "bool":
        """bool

        Args:
            design (mastapy.system_model.Design)
            sb (str)
        """
        sb = str(sb)
        method_result = self.wrapped.CompareForTestOnly(
            design.wrapped if design else None, sb if sb else ""
        )
        return method_result

    def add_bearing_detail_configuration_all_bearings(self: Self):
        """Method does not return."""
        self.wrapped.AddBearingDetailConfigurationAllBearings()

    def add_bearing_detail_configuration_rolling_bearings(self: Self):
        """Method does not return."""
        self.wrapped.AddBearingDetailConfigurationRollingBearings()

    def add_fe_substructure_configuration(self: Self):
        """Method does not return."""
        self.wrapped.AddFESubstructureConfiguration()

    def add_gear_set_configuration(self: Self):
        """Method does not return."""
        self.wrapped.AddGearSetConfiguration()

    def add_shaft_detail_configuration(self: Self):
        """Method does not return."""
        self.wrapped.AddShaftDetailConfiguration()

    def change_gears_to_clones_where_suitable(self: Self):
        """Method does not return."""
        self.wrapped.ChangeGearsToClonesWhereSuitable()

    def clear_undo_redo_stacks(self: Self):
        """Method does not return."""
        self.wrapped.ClearUndoRedoStacks()

    def delete_all_gear_set_configurations_that_have_errors_or_warnings(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings()

    def delete_all_gear_sets_designs_that_are_not_used_in_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations()

    def delete_all_inactive_gear_set_designs(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllInactiveGearSetDesigns()

    def delete_multiple_bearing_detail_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteMultipleBearingDetailConfigurations()

    def delete_multiple_fe_substructure_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteMultipleFESubstructureConfigurations()

    def delete_multiple_gear_set_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteMultipleGearSetConfigurations()

    def delete_multiple_shaft_detail_configurations(self: Self):
        """Method does not return."""
        self.wrapped.DeleteMultipleShaftDetailConfigurations()

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "Design._Cast_Design":
        return self._Cast_Design(self)
