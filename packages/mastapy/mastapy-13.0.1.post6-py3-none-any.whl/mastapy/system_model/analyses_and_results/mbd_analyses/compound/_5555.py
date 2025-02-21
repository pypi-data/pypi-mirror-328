"""ConceptCouplingCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConceptCouplingCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5407
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5627,
        _5529,
        _5608,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundMultibodyDynamicsAnalysis")


class ConceptCouplingCompoundMultibodyDynamicsAnalysis(
    _5566.CouplingCompoundMultibodyDynamicsAnalysis
):
    """ConceptCouplingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.CouplingCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptCouplingCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5407.ConceptCouplingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5407.ConceptCouplingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingCompoundMultibodyDynamicsAnalysis(self)
