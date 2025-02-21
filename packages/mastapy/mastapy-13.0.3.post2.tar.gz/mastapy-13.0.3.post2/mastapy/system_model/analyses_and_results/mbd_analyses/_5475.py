"""KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5472
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5433,
        _5460,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(
    _5472.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5472.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5472.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5433.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5460.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(
            self
        )
