"""ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.static_loads import _6844
    from mastapy.system_model.analyses_and_results.system_deflections import _2721
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7040,
        _7041,
        _7110,
        _7006,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConceptGearSetAdvancedTimeSteppingAnalysisForModulation")


class ConceptGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
):
    """ConceptGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConceptGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.GearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2522.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6844.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2721.ConceptGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7040.ConceptGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConceptGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7041.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConceptGearSetAdvancedTimeSteppingAnalysisForModulation(self)
