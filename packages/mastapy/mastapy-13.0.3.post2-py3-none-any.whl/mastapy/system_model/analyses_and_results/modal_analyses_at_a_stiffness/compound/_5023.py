"""BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5020,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4892,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5025,
        _5013,
        _5041,
        _5067,
        _5086,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"
)


class BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness(
    _5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
):
    """BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
            parent: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(
                _5013.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
        ) -> "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelDifferentialPlanetGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelDifferentialPlanetGearModalAnalysisAtAStiffness]

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
    ) -> "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness(
            self
        )
