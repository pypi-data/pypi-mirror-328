"""ClutchCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ClutchCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5401
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5627,
        _5529,
        _5608,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ClutchCompoundMultibodyDynamicsAnalysis")


class ClutchCompoundMultibodyDynamicsAnalysis(
    _5566.CouplingCompoundMultibodyDynamicsAnalysis
):
    """ClutchCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ClutchCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ClutchCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
            parent: "ClutchCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.CouplingCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
        ) -> "ClutchCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ClutchCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

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
    ) -> "List[_5401.ClutchMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchMultibodyDynamicsAnalysis]

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
    ) -> "List[_5401.ClutchMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchMultibodyDynamicsAnalysis]

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
    ) -> "ClutchCompoundMultibodyDynamicsAnalysis._Cast_ClutchCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ClutchCompoundMultibodyDynamicsAnalysis(self)
