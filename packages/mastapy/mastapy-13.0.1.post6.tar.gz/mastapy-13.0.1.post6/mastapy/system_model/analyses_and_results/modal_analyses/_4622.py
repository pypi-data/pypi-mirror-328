"""CylindricalGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CylindricalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.system_deflections import _2742
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4621,
        _4620,
        _4667,
        _4682,
        _4572,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetModalAnalysis")


class CylindricalGearSetModalAnalysis(_4637.GearSetModalAnalysis):
    """CylindricalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetModalAnalysis")

    class _Cast_CylindricalGearSetModalAnalysis:
        """Special nested class for casting CylindricalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
            parent: "CylindricalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_4637.GearSetModalAnalysis":
            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_4682.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_4572.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "_4667.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PlanetaryGearSetModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
        ) -> "CylindricalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6866.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

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
    ) -> "_2742.CylindricalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_modal_analysis(
        self: Self,
    ) -> "List[_4621.CylindricalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4620.CylindricalGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetModalAnalysis._Cast_CylindricalGearSetModalAnalysis":
        return self._Cast_CylindricalGearSetModalAnalysis(self)
