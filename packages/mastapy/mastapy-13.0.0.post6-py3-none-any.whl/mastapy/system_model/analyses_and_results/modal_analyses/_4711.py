"""WormGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "WormGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4710,
        _4709,
        _4681,
        _4571,
        _4661,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetModalAnalysis",)


Self = TypeVar("Self", bound="WormGearSetModalAnalysis")


class WormGearSetModalAnalysis(_4636.GearSetModalAnalysis):
    """WormGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetModalAnalysis")

    class _Cast_WormGearSetModalAnalysis:
        """Special nested class for casting WormGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
            parent: "WormGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4636.GearSetModalAnalysis":
            return self._parent._cast(_4636.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4681.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4571.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4571

            return self._parent._cast(_4571.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_4661.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis",
        ) -> "WormGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2552.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6984.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2837.WormGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears_modal_analysis(self: Self) -> "List[_4710.WormGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4709.WormGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetModalAnalysis._Cast_WormGearSetModalAnalysis":
        return self._Cast_WormGearSetModalAnalysis(self)
