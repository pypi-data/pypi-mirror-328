"""CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6206,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6064,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6212,
        _6182,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation"
)


class CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation(
    _6206.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
):
    """CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6206.GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6206.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

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
    ) -> "List[_6064.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6064.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
