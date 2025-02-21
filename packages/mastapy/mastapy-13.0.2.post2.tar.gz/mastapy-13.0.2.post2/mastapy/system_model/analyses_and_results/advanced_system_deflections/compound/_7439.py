"""ComponentCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7493,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7306,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7415,
        _7416,
        _7418,
        _7422,
        _7425,
        _7428,
        _7429,
        _7430,
        _7433,
        _7437,
        _7442,
        _7443,
        _7446,
        _7450,
        _7453,
        _7456,
        _7459,
        _7461,
        _7464,
        _7465,
        _7466,
        _7467,
        _7470,
        _7472,
        _7475,
        _7476,
        _7480,
        _7483,
        _7486,
        _7489,
        _7490,
        _7491,
        _7492,
        _7496,
        _7499,
        _7500,
        _7501,
        _7502,
        _7503,
        _7506,
        _7509,
        _7510,
        _7513,
        _7518,
        _7519,
        _7522,
        _7525,
        _7526,
        _7528,
        _7529,
        _7530,
        _7533,
        _7534,
        _7535,
        _7536,
        _7537,
        _7540,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundAdvancedSystemDeflection")


class ComponentCompoundAdvancedSystemDeflection(
    _7493.PartCompoundAdvancedSystemDeflection
):
    """ComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_ComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting ComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
            parent: "ComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7415.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7416.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(
                _7416.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7418.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def bearing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7422.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BearingCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7425.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(
                _7425.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7428.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7429.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(
                _7429.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7430.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(_7430.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bolt_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7433.BoltCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.BoltCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7437.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(_7437.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7443.ConceptGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7446.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(_7446.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7450.ConnectorCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7453.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7456.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(_7456.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7459.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(
                _7459.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7461.CylindricalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(
                _7461.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7464.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(
                _7464.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7465.DatumCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7466.ExternalCADModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7467.FaceGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7470.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(_7470.FEPartCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7472.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(_7472.GearCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7475.GuideDxfModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7476.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(_7476.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> (
            "_7480.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7483.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7486.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7489.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(_7489.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7490.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7492.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7499.PlanetCarrierCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7500.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(_7500.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7501.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(_7501.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7502.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(_7502.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7503.RingPinsCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(_7503.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7506.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7509.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(_7509.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7510.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7513.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7518.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7519.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7522.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7525.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7526.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7528.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7529.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7530.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7533.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7535.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7535,
            )

            return self._parent._cast(
                _7535.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7536.VirtualComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7537.WormGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7537,
            )

            return self._parent._cast(_7537.WormGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7540.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7540,
            )

            return self._parent._cast(
                _7540.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "ComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7306.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "List[_7306.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection":
        return self._Cast_ComponentCompoundAdvancedSystemDeflection(self)
