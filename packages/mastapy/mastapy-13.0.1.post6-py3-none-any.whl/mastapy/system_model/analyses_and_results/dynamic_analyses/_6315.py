"""CouplingDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6299,
        _6304,
        _6360,
        _6382,
        _6397,
        _6277,
        _6358,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7547,
        _7548,
        _7545,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingDynamicAnalysis")


class CouplingDynamicAnalysis(_6377.SpecialisedAssemblyDynamicAnalysis):
    """CouplingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingDynamicAnalysis")

    class _Cast_CouplingDynamicAnalysis:
        """Special nested class for casting CouplingDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
            parent: "CouplingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6377.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6277.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6358.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7547.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6299.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6304.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6360.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartToPartShearCouplingDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6382.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.SpringDamperDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6397.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.TorqueConverterDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "CouplingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis":
        return self._Cast_CouplingDynamicAnalysis(self)
