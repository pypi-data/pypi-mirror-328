"""CylindricalPlanetGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4775
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CylindricalPlanetGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4623
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4786,
        _4805,
        _4753,
        _4807,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundModalAnalysis")


class CylindricalPlanetGearCompoundModalAnalysis(
    _4775.CylindricalGearCompoundModalAnalysis
):
    """CylindricalPlanetGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundModalAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundModalAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
            parent: "CylindricalPlanetGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4775.CylindricalGearCompoundModalAnalysis":
            return self._parent._cast(_4775.CylindricalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4786.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4805.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4753.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_4807.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
        ) -> "CylindricalPlanetGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4623.CylindricalPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis]

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
    ) -> "List[_4623.CylindricalPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis]

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
    ) -> "CylindricalPlanetGearCompoundModalAnalysis._Cast_CylindricalPlanetGearCompoundModalAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundModalAnalysis(self)
