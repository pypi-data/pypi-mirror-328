"""StraightBevelDiffGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6960,
        _6961,
        _6816,
        _6849,
        _6896,
        _6953,
        _6807,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetLoadCase",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetLoadCase")


class StraightBevelDiffGearSetLoadCase(_6830.BevelGearSetLoadCase):
    """StraightBevelDiffGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSetLoadCase")

    class _Cast_StraightBevelDiffGearSetLoadCase:
        """Special nested class for casting StraightBevelDiffGearSetLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
            parent: "StraightBevelDiffGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6830.BevelGearSetLoadCase":
            return self._parent._cast(_6830.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6816.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6849.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6896.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6953.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6807.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(_6807.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
        ) -> "StraightBevelDiffGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSetLoadCase.TYPE"):
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
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6960.StraightBevelDiffGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase]

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
    def straight_bevel_diff_gears_load_case(
        self: Self,
    ) -> "List[_6960.StraightBevelDiffGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_load_case(
        self: Self,
    ) -> "List[_6961.StraightBevelDiffGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetLoadCase._Cast_StraightBevelDiffGearSetLoadCase":
        return self._Cast_StraightBevelDiffGearSetLoadCase(self)
