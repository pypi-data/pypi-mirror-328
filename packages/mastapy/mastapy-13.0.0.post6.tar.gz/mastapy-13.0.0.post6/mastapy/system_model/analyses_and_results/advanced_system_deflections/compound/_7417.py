"""BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7422,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7284,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7410,
        _7438,
        _7464,
        _7470,
        _7440,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7538, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"
)


class BevelDifferentialGearMeshCompoundAdvancedSystemDeflection(
    _7422.BevelGearMeshCompoundAdvancedSystemDeflection
):
    """BevelDifferentialGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    )

    class _Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
            parent: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7422.BevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7422.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7410.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7438.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(
                _7438.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7464.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7470.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7440.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(_7440.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7538.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
        ) -> "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "List[_7284.BevelDifferentialGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7284.BevelDifferentialGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearMeshAdvancedSystemDeflection]

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
    ) -> "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialGearMeshCompoundAdvancedSystemDeflection(
            self
        )
