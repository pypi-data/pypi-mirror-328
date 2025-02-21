"""BeltDriveModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5158,
        _5117,
        _5197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BeltDriveModalAnalysisAtASpeed")


class BeltDriveModalAnalysisAtASpeed(_5216.SpecialisedAssemblyModalAnalysisAtASpeed):
    """BeltDriveModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveModalAnalysisAtASpeed")

    class _Cast_BeltDriveModalAnalysisAtASpeed:
        """Special nested class for casting BeltDriveModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
            parent: "BeltDriveModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_5216.SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_5117.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_5197.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "_5158.CVTModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.CVTModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
        ) -> "BeltDriveModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveModalAnalysisAtASpeed.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "BeltDriveModalAnalysisAtASpeed._Cast_BeltDriveModalAnalysisAtASpeed":
        return self._Cast_BeltDriveModalAnalysisAtASpeed(self)
