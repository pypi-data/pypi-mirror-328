"""SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7037,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6964
    from mastapy.system_model.analyses_and_results.system_deflections import _2816
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7119,
        _7120,
        _7024,
        _7053,
        _7079,
        _7118,
        _7014,
        _7099,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7037.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7037.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7024.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2551.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6964.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2816.SpiralBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7119.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7120.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )
