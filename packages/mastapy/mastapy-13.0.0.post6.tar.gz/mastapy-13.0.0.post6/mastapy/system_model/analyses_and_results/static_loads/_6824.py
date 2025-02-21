"""BevelDifferentialGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6822,
        _6823,
        _6815,
        _6848,
        _6895,
        _6952,
        _6806,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetLoadCase")


class BevelDifferentialGearSetLoadCase(_6829.BevelGearSetLoadCase):
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
        ) -> "_6829.BevelGearSetLoadCase":
            return self._parent._cast(_6829.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6815.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6848.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6895.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6952.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6806.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

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
    def gears(self: Self) -> "List[_6822.BevelDifferentialGearLoadCase]":
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
    ) -> "List[_6822.BevelDifferentialGearLoadCase]":
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
    ) -> "List[_6823.BevelDifferentialGearMeshLoadCase]":
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
