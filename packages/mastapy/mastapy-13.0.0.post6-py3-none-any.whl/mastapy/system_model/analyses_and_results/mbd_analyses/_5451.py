"""KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5454,
        _5457,
        _5439,
        _5488,
        _5375,
        _5466,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
    _5412.ConicalGearSetMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5412.ConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5412.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5439.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5488.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(
                _5488.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5375.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375

            return self._parent._cast(_5375.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5466.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7548.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5454.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> (
            "_5457.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
                self
            )
        )
