"""ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6074,
        _6043,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation"
)


class ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation(
    _6045.CouplingConnectionHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6045.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6839.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

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
    ) -> "ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
