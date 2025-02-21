"""StraightBevelSunGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "StraightBevelSunGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2570
    from mastapy.system_model.analyses_and_results.system_deflections import _2841
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4610,
        _4598,
        _4626,
        _4657,
        _4679,
        _4618,
        _4683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearModalAnalysis")


class StraightBevelSunGearModalAnalysis(_4711.StraightBevelDiffGearModalAnalysis):
    """StraightBevelSunGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearModalAnalysis")

    class _Cast_StraightBevelSunGearModalAnalysis:
        """Special nested class for casting StraightBevelSunGearModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
            parent: "StraightBevelSunGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4711.StraightBevelDiffGearModalAnalysis":
            return self._parent._cast(_4711.StraightBevelDiffGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4610.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4598.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4626.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4657.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4679.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4618.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_4683.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
        ) -> "StraightBevelSunGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "_2841.StraightBevelSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection

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
    ) -> "StraightBevelSunGearModalAnalysis._Cast_StraightBevelSunGearModalAnalysis":
        return self._Cast_StraightBevelSunGearModalAnalysis(self)
