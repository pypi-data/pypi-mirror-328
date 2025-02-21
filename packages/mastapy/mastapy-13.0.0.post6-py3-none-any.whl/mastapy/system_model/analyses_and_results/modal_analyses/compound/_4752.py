"""ComponentCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4596
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4728,
        _4729,
        _4731,
        _4735,
        _4738,
        _4741,
        _4742,
        _4743,
        _4746,
        _4750,
        _4755,
        _4756,
        _4759,
        _4763,
        _4766,
        _4769,
        _4772,
        _4774,
        _4777,
        _4778,
        _4779,
        _4780,
        _4783,
        _4785,
        _4788,
        _4789,
        _4793,
        _4796,
        _4799,
        _4802,
        _4803,
        _4804,
        _4805,
        _4809,
        _4812,
        _4813,
        _4814,
        _4815,
        _4816,
        _4819,
        _4822,
        _4823,
        _4826,
        _4831,
        _4832,
        _4835,
        _4838,
        _4839,
        _4841,
        _4842,
        _4843,
        _4846,
        _4847,
        _4848,
        _4849,
        _4850,
        _4853,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundModalAnalysis")


class ComponentCompoundModalAnalysis(_4806.PartCompoundModalAnalysis):
    """ComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundModalAnalysis")

    class _Cast_ComponentCompoundModalAnalysis:
        """Special nested class for casting ComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
            parent: "ComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4806.PartCompoundModalAnalysis":
            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4728.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4729.AbstractShaftOrHousingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4731.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(_4731.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4735.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.BearingCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4738.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4741.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4742.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4743.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.BevelGearCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4746.BoltCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BoltCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4750.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4755.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4756.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4759.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4763.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectorCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4766.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4769.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4772.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4774.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4777.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4778.DatumCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4779.ExternalCADModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4780.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.FaceGearCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4783.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FEPartCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4785.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4788.GuideDxfModelCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4789.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4793.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4796.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4799.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4802.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4803.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4804.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4805.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4809.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(
                _4809.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planet_carrier_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4812.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4813.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4814.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4815.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4816.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4819.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RollingRingCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4822.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4823.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4826.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4831.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4832.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4835.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4838.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(
                _4838.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4839.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4841.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4842.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4843.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4846.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4847.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4848.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4849.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4850.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "_4853.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.ZerolBevelGearCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
        ) -> "ComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4596.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4596.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundModalAnalysis._Cast_ComponentCompoundModalAnalysis":
        return self._Cast_ComponentCompoundModalAnalysis(self)
