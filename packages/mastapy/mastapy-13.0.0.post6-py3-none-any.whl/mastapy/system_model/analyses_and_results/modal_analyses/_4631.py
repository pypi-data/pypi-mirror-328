"""FEPartModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "FEPartModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.system_deflections import _2757
    from mastapy.nodal_analysis.component_mode_synthesis import _231
    from mastapy.system_model.analyses_and_results.modal_analyses import _4596, _4661
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("FEPartModalAnalysis",)


Self = TypeVar("Self", bound="FEPartModalAnalysis")


class FEPartModalAnalysis(_4573.AbstractShaftOrHousingModalAnalysis):
    """FEPartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartModalAnalysis")

    class _Cast_FEPartModalAnalysis:
        """Special nested class for casting FEPartModalAnalysis to subclasses."""

        def __init__(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
            parent: "FEPartModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_4573.AbstractShaftOrHousingModalAnalysis":
            return self._parent._cast(_4573.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_4596.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_4661.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis",
        ) -> "FEPartModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartModalAnalysis._Cast_FEPartModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6887.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2757.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_full_fe_results(self: Self) -> "List[_231.ModalCMSResults]":
        """List[mastapy.nodal_analysis.component_mode_synthesis.ModalCMSResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalFullFEResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[FEPartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def calculate_all_strain_and_kinetic_energies(self: Self):
        """Method does not return."""
        self.wrapped.CalculateAllStrainAndKineticEnergies()

    def calculate_mode_shapes(self: Self):
        """Method does not return."""
        self.wrapped.CalculateModeShapes()

    def calculate_selected_strain_and_kinetic_energy(self: Self):
        """Method does not return."""
        self.wrapped.CalculateSelectedStrainAndKineticEnergy()

    @property
    def cast_to(self: Self) -> "FEPartModalAnalysis._Cast_FEPartModalAnalysis":
        return self._Cast_FEPartModalAnalysis(self)
