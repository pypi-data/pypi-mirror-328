"""MountableComponentModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "MountableComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.system_deflections import _2803
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4598,
        _4601,
        _4605,
        _4607,
        _4608,
        _4610,
        _4615,
        _4620,
        _4623,
        _4626,
        _4629,
        _4632,
        _4636,
        _4642,
        _4644,
        _4651,
        _4657,
        _4661,
        _4665,
        _4668,
        _4671,
        _4673,
        _4674,
        _4681,
        _4685,
        _4689,
        _4690,
        _4691,
        _4692,
        _4693,
        _4697,
        _4699,
        _4705,
        _4708,
        _4711,
        _4714,
        _4716,
        _4717,
        _4718,
        _4720,
        _4721,
        _4724,
        _4725,
        _4726,
        _4727,
        _4732,
        _4735,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentModalAnalysis",)


Self = TypeVar("Self", bound="MountableComponentModalAnalysis")


class MountableComponentModalAnalysis(_4618.ComponentModalAnalysis):
    """MountableComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentModalAnalysis")

    class _Cast_MountableComponentModalAnalysis:
        """Special nested class for casting MountableComponentModalAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            parent: "MountableComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4598.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4601.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4605.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4607.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4608.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4610.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelGearModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4615.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4620.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4623.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4626.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4629.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4632.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4636.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.CVTPulleyModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4642.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(_4642.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4644.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalPlanetGearModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4651.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.FaceGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4657.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.GearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4661.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4665.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4668.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4671.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4673.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4674.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.MeasurementComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4681.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4685.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4689.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4690.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4691.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4692.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4693.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4697.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4699.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.ShaftHubConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4705.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4708.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4711.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4714.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4716.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4717.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4718.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4720.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4721.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4721

            return self._parent._cast(_4721.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4724.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4724

            return self._parent._cast(_4724.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4725.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4726.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4727.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4732.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4732

            return self._parent._cast(_4732.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4735.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.ZerolBevelGearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "MountableComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2803.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

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
    ) -> "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis":
        return self._Cast_MountableComponentModalAnalysis(self)
