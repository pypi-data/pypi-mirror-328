"""InterMountableComponentConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4663
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4754,
        _4758,
        _4761,
        _4766,
        _4771,
        _4776,
        _4779,
        _4782,
        _4787,
        _4789,
        _4797,
        _4803,
        _4808,
        _4812,
        _4816,
        _4819,
        _4822,
        _4830,
        _4839,
        _4842,
        _4849,
        _4852,
        _4855,
        _4858,
        _4867,
        _4873,
        _4876,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundModalAnalysis")


class InterMountableComponentConnectionCompoundModalAnalysis(
    _4784.ConnectionCompoundModalAnalysis
):
    """InterMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
            parent: "InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(
                _4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4758.BeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4761.BevelDifferentialGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(
                _4761.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4766.BevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4771.ClutchConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4776.ConceptCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(
                _4776.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4779.ConceptGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4782.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.ConicalGearMeshCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4787.CouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4789.CVTBeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4797.CylindricalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(_4797.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4803.FaceGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4808.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4812.HypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4816.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(
                _4816.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(
                _4819.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(
                _4822.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4830.PartToPartShearCouplingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(
                _4830.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4839.RingPinsToDiscConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4842.RollingRingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.RollingRingConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4849.SpiralBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4852.SpringDamperConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4855.StraightBevelDiffGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(
                _4855.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4858.StraightBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(_4858.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4867.TorqueConverterConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4867,
            )

            return self._parent._cast(
                _4867.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4873.WormGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4873,
            )

            return self._parent._cast(_4873.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4876.ZerolBevelGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4876,
            )

            return self._parent._cast(_4876.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4663.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4663.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysis(self)
