"""CylindricalGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7465,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7322,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7471,
        _7441,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearMeshCompoundAdvancedSystemDeflection")


class CylindricalGearMeshCompoundAdvancedSystemDeflection(
    _7465.GearMeshCompoundAdvancedSystemDeflection
):
    """CylindricalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
            parent: "CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7465.GearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7441.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "CylindricalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CylindricalGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

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
    ) -> "List[_7322.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7322.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

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
    ) -> "CylindricalGearMeshCompoundAdvancedSystemDeflection._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_CylindricalGearMeshCompoundAdvancedSystemDeflection(self)
