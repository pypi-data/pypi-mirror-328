"""ConnectorAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConnectorAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7302,
        _7375,
        _7393,
        _7319,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorAdvancedSystemDeflection")


class ConnectorAdvancedSystemDeflection(
    _7374.MountableComponentAdvancedSystemDeflection
):
    """ConnectorAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorAdvancedSystemDeflection")

    class _Cast_ConnectorAdvancedSystemDeflection:
        """Special nested class for casting ConnectorAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
            parent: "ConnectorAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7374.MountableComponentAdvancedSystemDeflection":
            return self._parent._cast(_7374.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7302.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.BearingAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7375.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.OilSealAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "_7393.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "ConnectorAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection":
        return self._Cast_ConnectorAdvancedSystemDeflection(self)
