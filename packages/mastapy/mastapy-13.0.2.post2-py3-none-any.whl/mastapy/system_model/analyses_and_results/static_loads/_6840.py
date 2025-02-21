"""BoltLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltLoadCase",)


Self = TypeVar("Self", bound="BoltLoadCase")


class BoltLoadCase(_6846.ComponentLoadCase):
    """BoltLoadCase

    This is a mastapy class.
    """

    TYPE = _BOLT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltLoadCase")

    class _Cast_BoltLoadCase:
        """Special nested class for casting BoltLoadCase to subclasses."""

        def __init__(self: "BoltLoadCase._Cast_BoltLoadCase", parent: "BoltLoadCase"):
            self._parent = parent

        @property
        def component_load_case(
            self: "BoltLoadCase._Cast_BoltLoadCase",
        ) -> "_6846.ComponentLoadCase":
            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BoltLoadCase._Cast_BoltLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "BoltLoadCase._Cast_BoltLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltLoadCase._Cast_BoltLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltLoadCase._Cast_BoltLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolt_load_case(self: "BoltLoadCase._Cast_BoltLoadCase") -> "BoltLoadCase":
            return self._parent

        def __getattr__(self: "BoltLoadCase._Cast_BoltLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2449.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltLoadCase._Cast_BoltLoadCase":
        return self._Cast_BoltLoadCase(self)
