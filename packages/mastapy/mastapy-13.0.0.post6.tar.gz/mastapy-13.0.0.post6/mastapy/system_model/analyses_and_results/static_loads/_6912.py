"""KlingelnbergCycloPalloidConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6915,
        _6918,
        _6890,
        _6924,
        _6837,
        _6928,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearLoadCase")


class KlingelnbergCycloPalloidConicalGearLoadCase(_6844.ConicalGearLoadCase):
    """KlingelnbergCycloPalloidConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
            parent: "KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6844.ConicalGearLoadCase":
            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6890.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6924.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6837.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6928.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6915.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "KlingelnbergCycloPalloidConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase":
        return self._Cast_KlingelnbergCycloPalloidConicalGearLoadCase(self)
