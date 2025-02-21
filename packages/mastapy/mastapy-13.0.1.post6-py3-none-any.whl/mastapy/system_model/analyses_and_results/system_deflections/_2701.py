"""BevelDifferentialGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel import _554
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.static_loads import _6824
    from mastapy.system_model.analyses_and_results.power_flows import _4043
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2689,
        _2724,
        _2759,
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
__all__ = ("BevelDifferentialGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshSystemDeflection")


class BevelDifferentialGearMeshSystemDeflection(_2706.BevelGearMeshSystemDeflection):
    """BevelDifferentialGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshSystemDeflection"
    )

    class _Cast_BevelDifferentialGearMeshSystemDeflection:
        """Special nested class for casting BevelDifferentialGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
            parent: "BevelDifferentialGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2706.BevelGearMeshSystemDeflection":
            return self._parent._cast(_2706.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2689.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2724.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2759.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2727.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
        ) -> "BevelDifferentialGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_554.BevelGearMeshRating":
        """mastapy.gears.rating.bevel.BevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_554.BevelGearMeshRating":
        """mastapy.gears.rating.bevel.BevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

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
    def connection_load_case(self: Self) -> "_6824.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4043.BevelDifferentialGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearMeshPowerFlow

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
    ) -> "BevelDifferentialGearMeshSystemDeflection._Cast_BevelDifferentialGearMeshSystemDeflection":
        return self._Cast_BevelDifferentialGearMeshSystemDeflection(self)
