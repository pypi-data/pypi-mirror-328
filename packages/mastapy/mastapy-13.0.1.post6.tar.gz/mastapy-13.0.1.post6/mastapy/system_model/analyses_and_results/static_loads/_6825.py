"""BevelDifferentialGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6823,
        _6824,
        _6816,
        _6849,
        _6896,
        _6953,
        _6807,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetLoadCase")


class BevelDifferentialGearSetLoadCase(_6830.BevelGearSetLoadCase):
    """BevelDifferentialGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearSetLoadCase")

    class _Cast_BevelDifferentialGearSetLoadCase:
        """Special nested class for casting BevelDifferentialGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
            parent: "BevelDifferentialGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6830.BevelGearSetLoadCase":
            return self._parent._cast(_6830.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6816.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6849.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6896.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6953.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6807.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "BevelDifferentialGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sun_speeds_are_equal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SunSpeedsAreEqual

        if temp is None:
            return False

        return temp

    @sun_speeds_are_equal.setter
    @enforce_parameter_types
    def sun_speeds_are_equal(self: Self, value: "bool"):
        self.wrapped.SunSpeedsAreEqual = bool(value) if value is not None else False

    @property
    def assembly_design(self: Self) -> "_2516.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6823.BevelDifferentialGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_load_case(
        self: Self,
    ) -> "List[_6823.BevelDifferentialGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_load_case(
        self: Self,
    ) -> "List[_6824.BevelDifferentialGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase":
        return self._Cast_BevelDifferentialGearSetLoadCase(self)
