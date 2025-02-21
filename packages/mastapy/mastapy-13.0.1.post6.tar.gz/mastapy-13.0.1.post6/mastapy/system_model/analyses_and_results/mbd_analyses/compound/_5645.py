"""SynchroniserSleeveCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5507
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5568,
        _5606,
        _5554,
        _5608,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundMultibodyDynamicsAnalysis")


class SynchroniserSleeveCompoundMultibodyDynamicsAnalysis(
    _5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis
):
    """SynchroniserSleeveCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
            parent: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_5568.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
        ) -> "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_5507.SynchroniserSleeveMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserSleeveMultibodyDynamicsAnalysis]

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
    ) -> "List[_5507.SynchroniserSleeveMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserSleeveMultibodyDynamicsAnalysis]

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
    ) -> "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserSleeveCompoundMultibodyDynamicsAnalysis(self)
