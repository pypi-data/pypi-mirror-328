"""BearingMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BearingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2439
    from mastapy.system_model.analyses_and_results.static_loads import _6819
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5524
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5463,
        _5403,
        _5466,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BearingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BearingMultibodyDynamicsAnalysis")


class BearingMultibodyDynamicsAnalysis(_5414.ConnectorMultibodyDynamicsAnalysis):
    """BearingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEARING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingMultibodyDynamicsAnalysis")

    class _Cast_BearingMultibodyDynamicsAnalysis:
        """Special nested class for casting BearingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
            parent: "BearingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connector_multibody_dynamics_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_5414.ConnectorMultibodyDynamicsAnalysis":
            return self._parent._cast(_5414.ConnectorMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_5463.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_5403.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_5466.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_7548.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
        ) -> "BearingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ansiabma_adjusted_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_adjusted_rating_life_damage_rate_during_analysis(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeDamageRateDuringAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_damage_rate_during_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeDamageRateDuringAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAStaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_static_safety_factor_at_current_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAStaticSafetyFactorAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def force(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def force_angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def iso2812007_basic_rating_life_damage_during_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeDamageDuringAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_damage_during_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeDamageDuringAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def iso762006_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO762006SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def iso762006_safety_factor_at_current_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO762006SafetyFactorAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_damage_during_analysis(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeDamageDuringAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_damage_during_analysis(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeDamageDuringAnalysis
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_damage_rate(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner_at_current_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInnerAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer_at_current_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuterAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress_inner_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStressInnerSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress_inner_safety_factor_at_current_time(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStressInnerSafetyFactorAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress_outer_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStressOuterSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_static_contact_stress_outer_safety_factor_at_current_time(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStressOuterSafetyFactorAtCurrentTime

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_acceleration(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAcceleration

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_displacement(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_tilt(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeTilt

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_velocity(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeVelocity

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2439.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6819.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_dynamic_force(self: Self) -> "_5524.DynamicForceVector3DResult":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceVector3DResult

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakDynamicForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[BearingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BearingMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BearingMultibodyDynamicsAnalysis._Cast_BearingMultibodyDynamicsAnalysis":
        return self._Cast_BearingMultibodyDynamicsAnalysis(self)
