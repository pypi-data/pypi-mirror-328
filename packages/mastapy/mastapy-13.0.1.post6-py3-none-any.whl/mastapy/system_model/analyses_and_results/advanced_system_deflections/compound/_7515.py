"""StraightBevelGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7423,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7385,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7411,
        _7439,
        _7465,
        _7471,
        _7441,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundAdvancedSystemDeflection")


class StraightBevelGearMeshCompoundAdvancedSystemDeflection(
    _7423.BevelGearMeshCompoundAdvancedSystemDeflection
):
    """StraightBevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
            parent: "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7423.BevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7439.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7465.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7441.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2327.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2327.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

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
    ) -> "List[_7385.StraightBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7385.StraightBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearMeshAdvancedSystemDeflection]

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
    ) -> "StraightBevelGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelGearMeshCompoundAdvancedSystemDeflection(self)
