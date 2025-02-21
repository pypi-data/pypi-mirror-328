"""SpringDamperConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.static_loads import _6911, _6849
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionLoadCase",)


Self = TypeVar("Self", bound="SpringDamperConnectionLoadCase")


class SpringDamperConnectionLoadCase(_6851.CouplingConnectionLoadCase):
    """SpringDamperConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperConnectionLoadCase")

    class _Cast_SpringDamperConnectionLoadCase:
        """Special nested class for casting SpringDamperConnectionLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
            parent: "SpringDamperConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6851.CouplingConnectionLoadCase":
            return self._parent._cast(_6851.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6911.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_6849.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_connection_load_case(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
        ) -> "SpringDamperConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionLoadCase._Cast_SpringDamperConnectionLoadCase":
        return self._Cast_SpringDamperConnectionLoadCase(self)
