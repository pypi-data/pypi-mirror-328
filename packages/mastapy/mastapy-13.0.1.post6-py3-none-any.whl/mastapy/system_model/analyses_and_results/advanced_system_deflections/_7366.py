"""RingPinsToDiscConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.system_deflections import _2795
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7308,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionAdvancedSystemDeflection")


class RingPinsToDiscConnectionAdvancedSystemDeflection(
    _7340.InterMountableComponentConnectionAdvancedSystemDeflection
):
    """RingPinsToDiscConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionAdvancedSystemDeflection"
    )

    class _Cast_RingPinsToDiscConnectionAdvancedSystemDeflection:
        """Special nested class for casting RingPinsToDiscConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
            parent: "RingPinsToDiscConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_7340.InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent._cast(
                _7340.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_7308.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
        ) -> "RingPinsToDiscConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "RingPinsToDiscConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_number_of_pins_in_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageNumberOfPinsInContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6945.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2795.RingPinsToDiscConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection":
        return self._Cast_RingPinsToDiscConnectionAdvancedSystemDeflection(self)
