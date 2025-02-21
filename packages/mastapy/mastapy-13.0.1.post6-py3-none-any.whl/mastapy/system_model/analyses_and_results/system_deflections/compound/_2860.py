"""BeltConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BeltConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.system_deflections import _2699
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2891,
        _2886,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BeltConnectionCompoundSystemDeflection")


class BeltConnectionCompoundSystemDeflection(
    _2917.InterMountableComponentConnectionCompoundSystemDeflection
):
    """BeltConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundSystemDeflection"
    )

    class _Cast_BeltConnectionCompoundSystemDeflection:
        """Special nested class for casting BeltConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
            parent: "BeltConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_2917.InterMountableComponentConnectionCompoundSystemDeflection":
            return self._parent._cast(
                _2917.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_2886.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "_2891.CVTBeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def belt_connection_compound_system_deflection(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
        ) -> "BeltConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2699.BeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2699.BeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundSystemDeflection._Cast_BeltConnectionCompoundSystemDeflection":
        return self._Cast_BeltConnectionCompoundSystemDeflection(self)
