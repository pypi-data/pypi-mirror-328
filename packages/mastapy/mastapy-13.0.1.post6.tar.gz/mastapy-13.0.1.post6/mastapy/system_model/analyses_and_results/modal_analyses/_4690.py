"""StraightBevelDiffGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "StraightBevelDiffGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4695,
        _4696,
        _4577,
        _4605,
        _4636,
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearModalAnalysis")


class StraightBevelDiffGearModalAnalysis(_4589.BevelGearModalAnalysis):
    """StraightBevelDiffGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearModalAnalysis")

    class _Cast_StraightBevelDiffGearModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
            parent: "StraightBevelDiffGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4589.BevelGearModalAnalysis":
            return self._parent._cast(_4589.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4577.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4605.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4636.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4695.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "_4696.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelSunGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
        ) -> "StraightBevelDiffGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "_2815.StraightBevelDiffGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection

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
    ) -> "StraightBevelDiffGearModalAnalysis._Cast_StraightBevelDiffGearModalAnalysis":
        return self._Cast_StraightBevelDiffGearModalAnalysis(self)
