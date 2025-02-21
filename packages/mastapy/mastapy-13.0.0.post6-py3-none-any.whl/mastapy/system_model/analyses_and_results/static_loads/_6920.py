"""KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6918,
        _6919,
        _6848,
        _6895,
        _6952,
        _6806,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase")


class KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase(
    _6914.KlingelnbergCycloPalloidConicalGearSetLoadCase
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6914.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6848.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6895.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6952.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6806.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(
        self: Self,
    ) -> "List[_6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_load_case(
        self: Self,
    ) -> "List[_6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_load_case(
        self: Self,
    ) -> "List[_6919.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase(self)
