"""SynchroniserPartLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6968,
        _6971,
        _6925,
        _6838,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartLoadCase",)


Self = TypeVar("Self", bound="SynchroniserPartLoadCase")


class SynchroniserPartLoadCase(_6853.CouplingHalfLoadCase):
    """SynchroniserPartLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartLoadCase")

    class _Cast_SynchroniserPartLoadCase:
        """Special nested class for casting SynchroniserPartLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
            parent: "SynchroniserPartLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6853.CouplingHalfLoadCase":
            return self._parent._cast(_6853.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6968.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserHalfLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "_6971.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.SynchroniserSleeveLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase",
        ) -> "SynchroniserPartLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase":
        return self._Cast_SynchroniserPartLoadCase(self)
