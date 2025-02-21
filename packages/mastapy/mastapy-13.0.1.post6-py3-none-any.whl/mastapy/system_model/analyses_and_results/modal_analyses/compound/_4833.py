"""StraightBevelDiffGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelDiffGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.modal_analyses import _4690
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4839,
        _4840,
        _4732,
        _4760,
        _4786,
        _4805,
        _4753,
        _4807,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundModalAnalysis")


class StraightBevelDiffGearCompoundModalAnalysis(_4744.BevelGearCompoundModalAnalysis):
    """StraightBevelDiffGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundModalAnalysis"
    )

    class _Cast_StraightBevelDiffGearCompoundModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
            parent: "StraightBevelDiffGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4744.BevelGearCompoundModalAnalysis":
            return self._parent._cast(_4744.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4732.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4760.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4786.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4805.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4839.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4840.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "StraightBevelDiffGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearCompoundModalAnalysis.TYPE"
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4690.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4690.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundModalAnalysis(self)
