"""OilSealCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "OilSealCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5606,
        _5554,
        _5608,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="OilSealCompoundMultibodyDynamicsAnalysis")


class OilSealCompoundMultibodyDynamicsAnalysis(
    _5565.ConnectorCompoundMultibodyDynamicsAnalysis
):
    """OilSealCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_OilSealCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting OilSealCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
            parent: "OilSealCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.ConnectorCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5565.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
        ) -> "OilSealCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "OilSealCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

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
    ) -> "List[_5466.OilSealMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.OilSealMultibodyDynamicsAnalysis]

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
    ) -> "List[_5466.OilSealMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.OilSealMultibodyDynamicsAnalysis]

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
    ) -> "OilSealCompoundMultibodyDynamicsAnalysis._Cast_OilSealCompoundMultibodyDynamicsAnalysis":
        return self._Cast_OilSealCompoundMultibodyDynamicsAnalysis(self)
