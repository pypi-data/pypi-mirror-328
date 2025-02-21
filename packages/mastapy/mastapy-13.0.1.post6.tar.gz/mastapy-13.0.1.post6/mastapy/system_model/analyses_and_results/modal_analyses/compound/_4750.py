"""ClutchConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4766
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ClutchConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.modal_analyses import _4593
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4793,
        _4763,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ClutchConnectionCompoundModalAnalysis")


class ClutchConnectionCompoundModalAnalysis(
    _4766.CouplingConnectionCompoundModalAnalysis
):
    """ClutchConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionCompoundModalAnalysis"
    )

    class _Cast_ClutchConnectionCompoundModalAnalysis:
        """Special nested class for casting ClutchConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
            parent: "ClutchConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_4766.CouplingConnectionCompoundModalAnalysis":
            return self._parent._cast(_4766.CouplingConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_4793.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_4763.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
        ) -> "ClutchConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ClutchConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

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
    ) -> "List[_4593.ClutchConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis]

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
    ) -> "List[_4593.ClutchConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis]

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
    ) -> "ClutchConnectionCompoundModalAnalysis._Cast_ClutchConnectionCompoundModalAnalysis":
        return self._Cast_ClutchConnectionCompoundModalAnalysis(self)
