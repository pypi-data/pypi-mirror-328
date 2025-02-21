"""StraightBevelPlanetGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "StraightBevelPlanetGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.system_deflections import _2819
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4588,
        _4576,
        _4604,
        _4635,
        _4657,
        _4596,
        _4661,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearModalAnalysis")


class StraightBevelPlanetGearModalAnalysis(_4689.StraightBevelDiffGearModalAnalysis):
    """StraightBevelPlanetGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGearModalAnalysis")

    class _Cast_StraightBevelPlanetGearModalAnalysis:
        """Special nested class for casting StraightBevelPlanetGearModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
            parent: "StraightBevelPlanetGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4689.StraightBevelDiffGearModalAnalysis":
            return self._parent._cast(_4689.StraightBevelDiffGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4588.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4576.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4604.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4635.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4657.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4596.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_4661.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
        ) -> "StraightBevelPlanetGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2819.StraightBevelPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection

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
    ) -> "StraightBevelPlanetGearModalAnalysis._Cast_StraightBevelPlanetGearModalAnalysis":
        return self._Cast_StraightBevelPlanetGearModalAnalysis(self)
