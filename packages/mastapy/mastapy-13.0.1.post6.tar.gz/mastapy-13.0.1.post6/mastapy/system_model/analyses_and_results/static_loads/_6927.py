"""OilSealLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "OilSealLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6925,
        _6838,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealLoadCase",)


Self = TypeVar("Self", bound="OilSealLoadCase")


class OilSealLoadCase(_6851.ConnectorLoadCase):
    """OilSealLoadCase

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealLoadCase")

    class _Cast_OilSealLoadCase:
        """Special nested class for casting OilSealLoadCase to subclasses."""

        def __init__(
            self: "OilSealLoadCase._Cast_OilSealLoadCase", parent: "OilSealLoadCase"
        ):
            self._parent = parent

        @property
        def connector_load_case(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_6851.ConnectorLoadCase":
            return self._parent._cast(_6851.ConnectorLoadCase)

        @property
        def mountable_component_load_case(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_load_case(
            self: "OilSealLoadCase._Cast_OilSealLoadCase",
        ) -> "OilSealLoadCase":
            return self._parent

        def __getattr__(self: "OilSealLoadCase._Cast_OilSealLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "OilSealLoadCase._Cast_OilSealLoadCase":
        return self._Cast_OilSealLoadCase(self)
