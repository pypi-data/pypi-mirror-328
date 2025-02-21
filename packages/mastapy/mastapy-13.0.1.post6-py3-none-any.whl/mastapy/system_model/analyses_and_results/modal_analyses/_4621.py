"""CylindricalGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CylindricalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.system_deflections import _2745
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4623,
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearModalAnalysis")


class CylindricalGearModalAnalysis(_4636.GearModalAnalysis):
    """CylindricalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearModalAnalysis")

    class _Cast_CylindricalGearModalAnalysis:
        """Special nested class for casting CylindricalGearModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
            parent: "CylindricalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4636.GearModalAnalysis":
            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "_4623.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CylindricalPlanetGearModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
        ) -> "CylindricalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6862.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2745.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis]

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

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearModalAnalysis._Cast_CylindricalGearModalAnalysis":
        return self._Cast_CylindricalGearModalAnalysis(self)
