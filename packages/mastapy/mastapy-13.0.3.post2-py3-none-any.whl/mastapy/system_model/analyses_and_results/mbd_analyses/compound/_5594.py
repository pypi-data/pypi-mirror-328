"""CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5444
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5647,
        _5553,
        _5585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
)


class CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(
    _5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5574.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5444.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5444.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
