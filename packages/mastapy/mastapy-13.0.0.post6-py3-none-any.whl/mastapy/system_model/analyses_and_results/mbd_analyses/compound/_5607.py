"""PartCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PartCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5528,
        _5529,
        _5530,
        _5532,
        _5534,
        _5535,
        _5536,
        _5538,
        _5539,
        _5541,
        _5542,
        _5543,
        _5544,
        _5546,
        _5547,
        _5548,
        _5549,
        _5551,
        _5553,
        _5554,
        _5556,
        _5557,
        _5559,
        _5560,
        _5562,
        _5564,
        _5565,
        _5567,
        _5569,
        _5570,
        _5571,
        _5573,
        _5575,
        _5577,
        _5578,
        _5579,
        _5580,
        _5581,
        _5583,
        _5584,
        _5585,
        _5586,
        _5588,
        _5589,
        _5590,
        _5592,
        _5594,
        _5596,
        _5597,
        _5599,
        _5600,
        _5602,
        _5603,
        _5604,
        _5605,
        _5606,
        _5608,
        _5610,
        _5612,
        _5613,
        _5614,
        _5615,
        _5616,
        _5617,
        _5619,
        _5620,
        _5622,
        _5623,
        _5624,
        _5626,
        _5627,
        _5629,
        _5630,
        _5632,
        _5633,
        _5635,
        _5636,
        _5638,
        _5639,
        _5640,
        _5641,
        _5642,
        _5643,
        _5644,
        _5645,
        _5647,
        _5648,
        _5649,
        _5650,
        _5651,
        _5653,
        _5654,
        _5656,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartCompoundMultibodyDynamicsAnalysis")


class PartCompoundMultibodyDynamicsAnalysis(_7545.PartCompoundAnalysis):
    """PartCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PartCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PartCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
            parent: "PartCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5528.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5528,
            )

            return self._parent._cast(
                _5528.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5529.AbstractShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5530.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5532.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5534.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5534,
            )

            return self._parent._cast(
                _5534.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5535.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(_5535.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5536.BearingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5536,
            )

            return self._parent._cast(_5536.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5538.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(_5538.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5539.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(
                _5539.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5541.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5543.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5544.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(_5544.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5546.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5547.BoltCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5548.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(
                _5548.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5549.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(_5549.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5551.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(
                _5554.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5564.ConnectorCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(_5564.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(_5565.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5569.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(_5569.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(_5570.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5571.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(
                _5571.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5573.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(
                _5573.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5577.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5578.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5579.DatumCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(_5579.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ExternalCADModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(_5581.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.FEPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(_5584.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(
                _5585.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(_5586.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5588.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.GuideDxfModelCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(_5590.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5592.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5594.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5597.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5600.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5603.MassDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(_5603.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5604.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.OilSealCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(_5606.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5612.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(
                _5612.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.PointLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(_5614.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.PowerLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.RingPinsCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5619.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5622.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.ShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(_5623.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5624.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5626.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5633.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5640.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5641.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5645.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5647.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5649.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(_5651.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5654.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "PartCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PartCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5466.PartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis]

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
    ) -> "List[_5466.PartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis]

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
    ) -> "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PartCompoundMultibodyDynamicsAnalysis(self)
