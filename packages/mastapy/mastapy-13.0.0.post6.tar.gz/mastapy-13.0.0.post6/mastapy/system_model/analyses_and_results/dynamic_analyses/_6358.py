"""PartToPartShearCouplingConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PartToPartShearCouplingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343, _6311
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7539,
        _7540,
        _7537,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionDynamicAnalysis")


class PartToPartShearCouplingConnectionDynamicAnalysis(
    _6313.CouplingConnectionDynamicAnalysis
):
    """PartToPartShearCouplingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionDynamicAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionDynamicAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
            parent: "PartToPartShearCouplingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_6313.CouplingConnectionDynamicAnalysis":
            return self._parent._cast(_6313.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_6343.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_6311.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7539.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "PartToPartShearCouplingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(
        self: Self,
    ) -> "_6929.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionDynamicAnalysis(self)
