"""BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5544,
        _5532,
        _5560,
        _5586,
        _5605,
        _5553,
        _5607,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis"
)


class BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis(
    _5539.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
):
    """BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5539.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5539.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5544.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(_5544.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5532.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(_5586.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5553.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5392.BevelDifferentialSunGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialSunGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5392.BevelDifferentialSunGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialSunGearMultibodyDynamicsAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis(
            self
        )
