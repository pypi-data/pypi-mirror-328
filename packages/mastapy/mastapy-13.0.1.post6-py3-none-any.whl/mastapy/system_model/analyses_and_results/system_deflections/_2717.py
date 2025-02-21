"""ConceptCouplingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConceptCouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.power_flows import _4058
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2767,
        _2727,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionSystemDeflection")


class ConceptCouplingConnectionSystemDeflection(
    _2729.CouplingConnectionSystemDeflection
):
    """ConceptCouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionSystemDeflection"
    )

    class _Cast_ConceptCouplingConnectionSystemDeflection:
        """Special nested class for casting ConceptCouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
            parent: "ConceptCouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2729.CouplingConnectionSystemDeflection":
            return self._parent._cast(_2729.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2727.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
        ) -> "ConceptCouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionSystemDeflection.TYPE"
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
    def connection_load_case(self: Self) -> "_6839.ConceptCouplingConnectionLoadCase":
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
    def power_flow_results(self: Self) -> "_4058.ConceptCouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionSystemDeflection._Cast_ConceptCouplingConnectionSystemDeflection":
        return self._Cast_ConceptCouplingConnectionSystemDeflection(self)
