"""StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6024,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6960
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6012,
        _6040,
        _6066,
        _6073,
        _6042,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7540, _7537
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation(
    _6024.BevelGearMeshHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6024.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6024.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6012.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6073.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7540.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7537.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelDiffGearMesh":
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
    def connection_load_case(self: Self) -> "_6960.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

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
    ) -> "StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation(
            self
        )
