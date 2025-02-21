"""PlanetCarrierCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PlanetCarrierCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6433,
        _6487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundDynamicAnalysis")


class PlanetCarrierCompoundDynamicAnalysis(
    _6485.MountableComponentCompoundDynamicAnalysis
):
    """PlanetCarrierCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierCompoundDynamicAnalysis")

    class _Cast_PlanetCarrierCompoundDynamicAnalysis:
        """Special nested class for casting PlanetCarrierCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
            parent: "PlanetCarrierCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_6485.MountableComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_6433.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_6487.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
        ) -> "PlanetCarrierCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetCarrierCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

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
    ) -> "List[_6364.PlanetCarrierDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis]

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
    ) -> "List[_6364.PlanetCarrierDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis]

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
    ) -> "PlanetCarrierCompoundDynamicAnalysis._Cast_PlanetCarrierCompoundDynamicAnalysis":
        return self._Cast_PlanetCarrierCompoundDynamicAnalysis(self)
