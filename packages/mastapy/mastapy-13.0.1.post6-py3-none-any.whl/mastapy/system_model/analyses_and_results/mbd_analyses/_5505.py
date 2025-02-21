"""SynchroniserMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5489
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6969
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5376, _5467
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserMultibodyDynamicsAnalysis")


class SynchroniserMultibodyDynamicsAnalysis(
    _5489.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """SynchroniserMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
            parent: "SynchroniserMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_5489.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5489.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_5376.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(_5376.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_5467.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_7549.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
        ) -> "SynchroniserMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2602.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6969.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserMultibodyDynamicsAnalysis._Cast_SynchroniserMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserMultibodyDynamicsAnalysis(self)
