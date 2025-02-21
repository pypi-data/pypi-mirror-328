"""FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5648
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5550,
        _5629,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis")


class FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis(
    _5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
):
    """FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5648.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5550.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2474.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2474.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_5457.FlexiblePinAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FlexiblePinAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5457.FlexiblePinAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FlexiblePinAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis(self)
