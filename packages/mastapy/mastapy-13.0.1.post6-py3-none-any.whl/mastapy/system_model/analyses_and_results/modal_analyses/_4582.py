"""BeltDriveModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BeltDriveModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.system_deflections import _2700
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4614,
        _4572,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveModalAnalysis",)


Self = TypeVar("Self", bound="BeltDriveModalAnalysis")


class BeltDriveModalAnalysis(_4682.SpecialisedAssemblyModalAnalysis):
    """BeltDriveModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveModalAnalysis")

    class _Cast_BeltDriveModalAnalysis:
        """Special nested class for casting BeltDriveModalAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
            parent: "BeltDriveModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_4682.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_4572.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "_4614.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CVTModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis",
        ) -> "BeltDriveModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2700.BeltDriveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BeltDriveModalAnalysis._Cast_BeltDriveModalAnalysis":
        return self._Cast_BeltDriveModalAnalysis(self)
