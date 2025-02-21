"""PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6713,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6740,
        _6710,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"
)


class PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis(
    _6713.CouplingConnectionCompoundCriticalSpeedAnalysis
):
    """PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
            parent: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6713.CouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6713.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2348.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6626.PartToPartShearCouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PartToPartShearCouplingConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6626.PartToPartShearCouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PartToPartShearCouplingConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )
