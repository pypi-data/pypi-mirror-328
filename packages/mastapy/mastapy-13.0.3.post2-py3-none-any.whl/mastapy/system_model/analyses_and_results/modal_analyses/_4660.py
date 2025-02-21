"""HypoidGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "HypoidGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.system_deflections import _2784
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4625,
        _4656,
        _4663,
        _4628,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshModalAnalysis")


class HypoidGearMeshModalAnalysis(_4597.AGMAGleasonConicalGearMeshModalAnalysis):
    """HypoidGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshModalAnalysis")

    class _Cast_HypoidGearMeshModalAnalysis:
        """Special nested class for casting HypoidGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
            parent: "HypoidGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_4597.AGMAGleasonConicalGearMeshModalAnalysis":
            return self._parent._cast(_4597.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_4625.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_4656.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_4663.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(
                _4663.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_4628.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
        ) -> "HypoidGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6928.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2784.HypoidGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshModalAnalysis._Cast_HypoidGearMeshModalAnalysis":
        return self._Cast_HypoidGearMeshModalAnalysis(self)
