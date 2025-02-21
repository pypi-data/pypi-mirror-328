"""ConceptCouplingConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.static_loads import _6838
    from mastapy.system_model.analyses_and_results.system_deflections import _2717
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7339,
        _7307,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionAdvancedSystemDeflection")


class ConceptCouplingConnectionAdvancedSystemDeflection(
    _7311.CouplingConnectionAdvancedSystemDeflection
):
    """ConceptCouplingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionAdvancedSystemDeflection"
    )

    class _Cast_ConceptCouplingConnectionAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
            parent: "ConceptCouplingConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_system_deflection(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_7311.CouplingConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7311.CouplingConnectionAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_7339.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_7307.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
        ) -> "ConceptCouplingConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptCouplingConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6838.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

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
    ) -> "List[_2717.ConceptCouplingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection]

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
    ) -> "ConceptCouplingConnectionAdvancedSystemDeflection._Cast_ConceptCouplingConnectionAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingConnectionAdvancedSystemDeflection(self)
