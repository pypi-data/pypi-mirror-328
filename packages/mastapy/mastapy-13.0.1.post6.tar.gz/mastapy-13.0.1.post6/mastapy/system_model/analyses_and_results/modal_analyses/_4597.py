"""ComponentModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4662
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.analyses_and_results.system_deflections import _2715
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4573,
        _4574,
        _4577,
        _4580,
        _4584,
        _4586,
        _4587,
        _4589,
        _4592,
        _4594,
        _4599,
        _4602,
        _4605,
        _4608,
        _4611,
        _4615,
        _4618,
        _4621,
        _4623,
        _4624,
        _4628,
        _4630,
        _4632,
        _4636,
        _4638,
        _4640,
        _4644,
        _4647,
        _4650,
        _4652,
        _4653,
        _4658,
        _4660,
        _4664,
        _4668,
        _4669,
        _4670,
        _4671,
        _4672,
        _4676,
        _4678,
        _4679,
        _4684,
        _4687,
        _4690,
        _4693,
        _4695,
        _4696,
        _4697,
        _4699,
        _4700,
        _4703,
        _4704,
        _4705,
        _4706,
        _4711,
        _4714,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentModalAnalysis",)


Self = TypeVar("Self", bound="ComponentModalAnalysis")


class ComponentModalAnalysis(_4662.PartModalAnalysis):
    """ComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentModalAnalysis")

    class _Cast_ComponentModalAnalysis:
        """Special nested class for casting ComponentModalAnalysis to subclasses."""

        def __init__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
            parent: "ComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4573.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4574.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4577.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4580.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4584.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4586.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4587.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4589.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelGearModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4592.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4594.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4599.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4602.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4605.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4608.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4611.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4615.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CVTPulleyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4618.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4621.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4623.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4624.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4628.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4630.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.FaceGearModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4632.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FEPartModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4636.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4638.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4640.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4644.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4647.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4650.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4652.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(_4652.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4653.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4660.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4664.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4668.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4669.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4670.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4671.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4672.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4676.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4678.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4679.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.ShaftModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4684.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4687.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4690.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4693.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4695.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4696.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4697.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4699.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4700.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4703.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4704.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4705.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4706.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4711.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4714.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.ZerolBevelGearModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "ComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2444.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2715.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentModalAnalysis._Cast_ComponentModalAnalysis":
        return self._Cast_ComponentModalAnalysis(self)
