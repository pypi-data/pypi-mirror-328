"""ConceptGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConceptGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5627,
        _5575,
        _5629,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptGearCompoundMultibodyDynamicsAnalysis")


class ConceptGearCompoundMultibodyDynamicsAnalysis(
    _5608.GearCompoundMultibodyDynamicsAnalysis
):
    """ConceptGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
            parent: "ConceptGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.GearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5608.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(_5575.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
        ) -> "ConceptGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5430.ConceptGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptGearMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5430.ConceptGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptGearMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ConceptGearCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConceptGearCompoundMultibodyDynamicsAnalysis(self)
