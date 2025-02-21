"""ZerolBevelGearMeshCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ZerolBevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.system_deflections import _2839
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2856,
        _2884,
        _2911,
        _2917,
        _2886,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundSystemDeflection")


class ZerolBevelGearMeshCompoundSystemDeflection(
    _2868.BevelGearMeshCompoundSystemDeflection
):
    """ZerolBevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundSystemDeflection"
    )

    class _Cast_ZerolBevelGearMeshCompoundSystemDeflection:
        """Special nested class for casting ZerolBevelGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
            parent: "ZerolBevelGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2868.BevelGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2868.BevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2856.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2856,
            )

            return self._parent._cast(
                _2856.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2884.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2911.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2917.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2886.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "ZerolBevelGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_2839.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

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
    ) -> "List[_2839.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

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
    ) -> "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection":
        return self._Cast_ZerolBevelGearMeshCompoundSystemDeflection(self)
