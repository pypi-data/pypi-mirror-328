"""PowerLoadAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7155,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.system_deflections import _2813
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7110,
        _7057,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="PowerLoadAdvancedTimeSteppingAnalysisForModulation")


class PowerLoadAdvancedTimeSteppingAnalysisForModulation(
    _7155.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
):
    """PowerLoadAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PowerLoadAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
            parent: "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7155.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7155.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PowerLoadAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2492.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6961.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2813.PowerLoadSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection

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
    ) -> "PowerLoadAdvancedTimeSteppingAnalysisForModulation._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PowerLoadAdvancedTimeSteppingAnalysisForModulation(self)
