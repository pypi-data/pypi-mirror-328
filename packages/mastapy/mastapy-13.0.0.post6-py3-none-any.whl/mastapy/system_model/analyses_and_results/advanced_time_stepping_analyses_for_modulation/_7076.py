"""InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281
    from mastapy.system_model.analyses_and_results.system_deflections import _2767
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7014,
        _7019,
        _7022,
        _7027,
        _7032,
        _7037,
        _7040,
        _7043,
        _7048,
        _7051,
        _7058,
        _7064,
        _7069,
        _7074,
        _7078,
        _7081,
        _7084,
        _7092,
        _7101,
        _7104,
        _7111,
        _7114,
        _7117,
        _7120,
        _7129,
        _7135,
        _7138,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7045.ConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7045.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7014.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7019.BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7019,
            )

            return self._parent._cast(
                _7019.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7022.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7027.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7032.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7043.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7051.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7064.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7074.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7081.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7084.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7101.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7104.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7111.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7114.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7120.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2281.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection

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
    ) -> "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
