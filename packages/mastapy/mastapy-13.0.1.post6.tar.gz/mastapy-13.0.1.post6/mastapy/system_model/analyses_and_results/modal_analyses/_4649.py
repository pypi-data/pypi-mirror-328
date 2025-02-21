"""KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4643
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.static_loads import _6920
    from mastapy.system_model.analyses_and_results.system_deflections import _2774
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4604,
        _4635,
        _4642,
        _4607,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis")


class KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis(
    _4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_4604.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_4635.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_4642.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_4607.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2320.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6920.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2774.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis(self)
