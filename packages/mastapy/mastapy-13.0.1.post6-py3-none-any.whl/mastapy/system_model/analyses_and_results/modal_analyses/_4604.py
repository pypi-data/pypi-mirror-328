"""ConicalGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4635
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConicalGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2307
    from mastapy.system_model.analyses_and_results.system_deflections import _2724
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4576,
        _4583,
        _4588,
        _4639,
        _4643,
        _4646,
        _4649,
        _4683,
        _4689,
        _4692,
        _4713,
        _4642,
        _4607,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshModalAnalysis")


class ConicalGearMeshModalAnalysis(_4635.GearMeshModalAnalysis):
    """ConicalGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshModalAnalysis")

    class _Cast_ConicalGearMeshModalAnalysis:
        """Special nested class for casting ConicalGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
            parent: "ConicalGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4635.GearMeshModalAnalysis":
            return self._parent._cast(_4635.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4642.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4607.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4576.AGMAGleasonConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4583.BevelDifferentialGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4588.BevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelGearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4639.HypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.HypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4646.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4649.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(
                _4649.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4683.SpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4689.StraightBevelDiffGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4692.StraightBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "_4713.ZerolBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.ZerolBevelGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
        ) -> "ConicalGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis]

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
    def system_deflection_results(
        self: Self,
    ) -> "_2724.ConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection

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
    ) -> "ConicalGearMeshModalAnalysis._Cast_ConicalGearMeshModalAnalysis":
        return self._Cast_ConicalGearMeshModalAnalysis(self)
