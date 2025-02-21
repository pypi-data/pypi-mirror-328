"""BevelDifferentialGearMeshCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4766
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.modal_analyses import _4604
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4754,
        _4782,
        _4808,
        _4814,
        _4784,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundModalAnalysis")


class BevelDifferentialGearMeshCompoundModalAnalysis(
    _4766.BevelGearMeshCompoundModalAnalysis
):
    """BevelDifferentialGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshCompoundModalAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
            parent: "BevelDifferentialGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4766.BevelGearMeshCompoundModalAnalysis":
            return self._parent._cast(_4766.BevelGearMeshCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(
                _4754.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4782.ConicalGearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4808.GearMeshCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4814.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(
                _4814.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_4784.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
        ) -> "BevelDifferentialGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2321.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "List[_4604.BevelDifferentialGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis]

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
    ) -> "List[_4604.BevelDifferentialGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis]

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
    ) -> "BevelDifferentialGearMeshCompoundModalAnalysis._Cast_BevelDifferentialGearMeshCompoundModalAnalysis":
        return self._Cast_BevelDifferentialGearMeshCompoundModalAnalysis(self)
