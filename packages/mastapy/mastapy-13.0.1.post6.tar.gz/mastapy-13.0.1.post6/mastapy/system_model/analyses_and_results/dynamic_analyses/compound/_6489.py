"""PartToPartShearCouplingConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6473,
        _6443,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionCompoundDynamicAnalysis")


class PartToPartShearCouplingConnectionCompoundDynamicAnalysis(
    _6446.CouplingConnectionCompoundDynamicAnalysis
):
    """PartToPartShearCouplingConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
            parent: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6446.CouplingConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6446.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6473.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_6443.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
        ) -> "PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundDynamicAnalysis.TYPE",
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
    ) -> "List[_6359.PartToPartShearCouplingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis]

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
    ) -> "List[_6359.PartToPartShearCouplingConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis]

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
    ) -> "PartToPartShearCouplingConnectionCompoundDynamicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionCompoundDynamicAnalysis(self)
