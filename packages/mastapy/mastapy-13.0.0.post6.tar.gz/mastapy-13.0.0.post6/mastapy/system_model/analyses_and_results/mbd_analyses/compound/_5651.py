"""WormGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "WormGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5517
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5605,
        _5553,
        _5607,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("WormGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="WormGearCompoundMultibodyDynamicsAnalysis")


class WormGearCompoundMultibodyDynamicsAnalysis(
    _5586.GearCompoundMultibodyDynamicsAnalysis
):
    """WormGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_WormGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting WormGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
            parent: "WormGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.GearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5586.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
        ) -> "WormGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "WormGearCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

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
    ) -> "List[_5517.WormGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5517.WormGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearMultibodyDynamicsAnalysis]

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
    ) -> "WormGearCompoundMultibodyDynamicsAnalysis._Cast_WormGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_WormGearCompoundMultibodyDynamicsAnalysis(self)
