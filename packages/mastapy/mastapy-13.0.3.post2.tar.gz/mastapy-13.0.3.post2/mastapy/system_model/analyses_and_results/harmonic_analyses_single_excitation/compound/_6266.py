"""StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6177,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2345
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6137,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6165,
        _6193,
        _6219,
        _6225,
        _6195,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation(
    _6177.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = (
        _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6177.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6177.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6165.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6193.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6219.GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2345.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

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
    ) -> "List[_6137.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6137.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
