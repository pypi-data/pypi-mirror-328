"""AGMAGleasonConicalGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2299
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7285,
        _7290,
        _7338,
        _7376,
        _7382,
        _7385,
        _7404,
        _7334,
        _7340,
        _7308,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshAdvancedSystemDeflection")


class AGMAGleasonConicalGearMeshAdvancedSystemDeflection(
    _7306.ConicalGearMeshAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7306.ConicalGearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7306.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7334.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7340.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7308.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7285.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7290.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.BevelGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7338.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7376.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7382.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7385.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "_7404.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection(self)
