"""ConceptGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConceptGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.gears.rating.concept import _554
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.power_flows import _4083
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2803,
        _2736,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearSystemDeflection")


class ConceptGearSystemDeflection(_2782.GearSystemDeflection):
    """ConceptGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSystemDeflection")

    class _Cast_ConceptGearSystemDeflection:
        """Special nested class for casting ConceptGearSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
            parent: "ConceptGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_system_deflection(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2782.GearSystemDeflection":
            return self._parent._cast(_2782.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2803.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2736.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_system_deflection(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
        ) -> "ConceptGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_554.ConceptGearRating":
        """mastapy.gears.rating.concept.ConceptGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6863.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4083.ConceptGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConceptGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSystemDeflection._Cast_ConceptGearSystemDeflection":
        return self._Cast_ConceptGearSystemDeflection(self)
