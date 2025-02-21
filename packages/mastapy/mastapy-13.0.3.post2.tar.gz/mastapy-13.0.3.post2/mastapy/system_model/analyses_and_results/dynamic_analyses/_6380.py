"""PartToPartShearCouplingConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PartToPartShearCouplingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365, _6333
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionDynamicAnalysis")


class PartToPartShearCouplingConnectionDynamicAnalysis(
    _6335.CouplingConnectionDynamicAnalysis
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
        ) -> "_6335.CouplingConnectionDynamicAnalysis":
            return self._parent._cast(_6335.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_6365.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(
                _6365.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_6333.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionDynamicAnalysis._Cast_PartToPartShearCouplingConnectionDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def connection_design(self: Self) -> "_2368.PartToPartShearCouplingConnection":
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
    ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
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
