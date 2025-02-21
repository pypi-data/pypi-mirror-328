"""BevelGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4590
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4741,
        _4829,
        _4835,
        _4838,
        _4856,
        _4762,
        _4788,
        _4826,
        _4728,
        _4807,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundModalAnalysis")


class BevelGearSetCompoundModalAnalysis(
    _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
):
    """BevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundModalAnalysis")

    class _Cast_BevelGearSetCompoundModalAnalysis:
        """Special nested class for casting BevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
            parent: "BevelGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4734.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4762.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4788.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4826.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4728.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4741.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4829.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4835.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4838.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4856.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "BevelGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4590.BevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4590.BevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis":
        return self._Cast_BevelGearSetCompoundModalAnalysis(self)
