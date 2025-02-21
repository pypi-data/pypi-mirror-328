"""MountableComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3809
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "MountableComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3790,
        _3792,
        _3797,
        _3798,
        _3799,
        _3802,
        _3806,
        _3811,
        _3815,
        _3818,
        _3820,
        _3822,
        _3826,
        _3834,
        _3835,
        _3841,
        _3846,
        _3850,
        _3854,
        _3857,
        _3860,
        _3861,
        _3862,
        _3864,
        _3867,
        _3871,
        _3872,
        _3873,
        _3874,
        _3875,
        _3879,
        _3881,
        _3887,
        _3889,
        _3896,
        _3899,
        _3900,
        _3901,
        _3902,
        _3903,
        _3904,
        _3907,
        _3909,
        _3910,
        _3911,
        _3914,
        _3917,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="MountableComponentStabilityAnalysis")


class MountableComponentStabilityAnalysis(_3809.ComponentStabilityAnalysis):
    """MountableComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentStabilityAnalysis")

    class _Cast_MountableComponentStabilityAnalysis:
        """Special nested class for casting MountableComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
            parent: "MountableComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3790.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3792.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.BearingStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3797.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3798.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(
                _3798.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3799.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3802.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.BevelGearStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3806.ClutchHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3811.ConceptCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3815.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3818.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3820.ConnectorStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3822.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.CouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3826.CVTPulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.CVTPulleyStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3834.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(_3834.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3835.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(_3835.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3841.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.FaceGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3850.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3854.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(
                _3854.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3857.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(
                _3857.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3860.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3861.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3862.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.MeasurementComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3864.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3867.PartToPartShearCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(
                _3867.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def planet_carrier_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3871.PlanetCarrierStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3872.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3873.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3874.PulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3875.RingPinsStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3879.RollingRingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3881.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.ShaftHubConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3887.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3889.SpringDamperHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3896.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3899.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3899,
            )

            return self._parent._cast(_3899.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3900.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3901.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3901,
            )

            return self._parent._cast(_3901.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3902.SynchroniserHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3902,
            )

            return self._parent._cast(_3902.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3903.SynchroniserPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3904.SynchroniserSleeveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3904,
            )

            return self._parent._cast(_3904.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3907.TorqueConverterPumpStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3907,
            )

            return self._parent._cast(_3907.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3909.TorqueConverterTurbineStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3909,
            )

            return self._parent._cast(_3909.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3910.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3910,
            )

            return self._parent._cast(_3910.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3911.VirtualComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3911,
            )

            return self._parent._cast(_3911.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3914.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3914,
            )

            return self._parent._cast(_3914.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3917.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3917,
            )

            return self._parent._cast(_3917.ZerolBevelGearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "MountableComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis"
    ):
        return self._Cast_MountableComponentStabilityAnalysis(self)
