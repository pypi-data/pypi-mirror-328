"""BevelDifferentialGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelDifferentialGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.modal_analyses import _4584
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4742,
        _4743,
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
__all__ = ("BevelDifferentialGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundModalAnalysis")


class BevelDifferentialGearCompoundModalAnalysis(_4744.BevelGearCompoundModalAnalysis):
    """BevelDifferentialGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundModalAnalysis"
    )

    class _Cast_BevelDifferentialGearCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
            parent: "BevelDifferentialGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4744.BevelGearCompoundModalAnalysis":
            return self._parent._cast(_4744.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4732.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4760.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4786.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4805.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4742.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "_4743.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
        ) -> "BevelDifferentialGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "List[_4584.BevelDifferentialGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis]

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
    ) -> "List[_4584.BevelDifferentialGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis]

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
    ) -> "BevelDifferentialGearCompoundModalAnalysis._Cast_BevelDifferentialGearCompoundModalAnalysis":
        return self._Cast_BevelDifferentialGearCompoundModalAnalysis(self)
