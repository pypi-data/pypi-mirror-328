"""SpringDamperConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5493
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5594,
        _5564,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7539, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundMultibodyDynamicsAnalysis")


class SpringDamperConnectionCompoundMultibodyDynamicsAnalysis(
    _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
):
    """SpringDamperConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5564.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(_5564.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7539.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2350.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_5493.SpringDamperConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpringDamperConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5493.SpringDamperConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpringDamperConnectionMultibodyDynamicsAnalysis]

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
    ) -> "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpringDamperConnectionCompoundMultibodyDynamicsAnalysis(self)
