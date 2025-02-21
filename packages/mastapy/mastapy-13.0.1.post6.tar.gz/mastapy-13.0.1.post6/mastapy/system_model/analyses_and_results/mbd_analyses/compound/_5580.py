"""DatumCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "DatumCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("DatumCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="DatumCompoundMultibodyDynamicsAnalysis")


class DatumCompoundMultibodyDynamicsAnalysis(
    _5554.ComponentCompoundMultibodyDynamicsAnalysis
):
    """DatumCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DatumCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_DatumCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting DatumCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
            parent: "DatumCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
        ) -> "DatumCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "DatumCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2448.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5430.DatumMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.DatumMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5430.DatumMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.DatumMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "DatumCompoundMultibodyDynamicsAnalysis._Cast_DatumCompoundMultibodyDynamicsAnalysis":
        return self._Cast_DatumCompoundMultibodyDynamicsAnalysis(self)
