"""RingPinsCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "RingPinsCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5477
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5554,
        _5608,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RingPinsCompoundMultibodyDynamicsAnalysis")


class RingPinsCompoundMultibodyDynamicsAnalysis(
    _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """RingPinsCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_RingPinsCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting RingPinsCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
            parent: "RingPinsCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
        ) -> "RingPinsCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

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
    ) -> "List[_5477.RingPinsMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RingPinsMultibodyDynamicsAnalysis]

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
    ) -> "List[_5477.RingPinsMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RingPinsMultibodyDynamicsAnalysis]

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
    ) -> "RingPinsCompoundMultibodyDynamicsAnalysis._Cast_RingPinsCompoundMultibodyDynamicsAnalysis":
        return self._Cast_RingPinsCompoundMultibodyDynamicsAnalysis(self)
