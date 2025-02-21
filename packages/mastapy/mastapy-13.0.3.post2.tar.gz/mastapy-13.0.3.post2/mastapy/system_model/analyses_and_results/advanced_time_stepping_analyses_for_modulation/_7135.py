"""SpringDamperAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2621
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.system_deflections import _2833
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7131,
        _7027,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="SpringDamperAdvancedTimeSteppingAnalysisForModulation")


class SpringDamperAdvancedTimeSteppingAnalysisForModulation(
    _7069.CouplingAdvancedTimeSteppingAnalysisForModulation
):
    """SpringDamperAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpringDamperAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.CouplingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7069.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7027.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpringDamperAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpringDamperAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2621.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6980.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2833.SpringDamperSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperAdvancedTimeSteppingAnalysisForModulation._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpringDamperAdvancedTimeSteppingAnalysisForModulation(self)
