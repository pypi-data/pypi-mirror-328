"""CouplingConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6074,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6029,
        _6034,
        _6090,
        _6112,
        _6127,
        _6043,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7538
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingConnectionHarmonicAnalysisOfSingleExcitation")


class CouplingConnectionHarmonicAnalysisOfSingleExcitation(
    _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """CouplingConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.ClutchConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6090.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6112.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "_6127.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingConnectionHarmonicAnalysisOfSingleExcitation(self)
