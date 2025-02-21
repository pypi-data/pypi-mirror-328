"""CouplingModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "CouplingModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.system_deflections import _2752
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4616,
        _4621,
        _4686,
        _4709,
        _4723,
        _4593,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysis",)


Self = TypeVar("Self", bound="CouplingModalAnalysis")


class CouplingModalAnalysis(_4703.SpecialisedAssemblyModalAnalysis):
    """CouplingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysis")

    class _Cast_CouplingModalAnalysis:
        """Special nested class for casting CouplingModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
            parent: "CouplingModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4703.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4703.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4593.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4616.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4621.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.ConceptCouplingModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4686.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.PartToPartShearCouplingModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4709.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.SpringDamperModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4723.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.TorqueConverterModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "CouplingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.Coupling":
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
    def system_deflection_results(self: Self) -> "_2752.CouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingModalAnalysis._Cast_CouplingModalAnalysis":
        return self._Cast_CouplingModalAnalysis(self)
