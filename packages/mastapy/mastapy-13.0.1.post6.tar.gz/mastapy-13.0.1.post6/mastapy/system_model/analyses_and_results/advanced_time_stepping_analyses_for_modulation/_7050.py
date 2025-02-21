"""CouplingHalfAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7089,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.system_deflections import _2730
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7034,
        _7039,
        _7053,
        _7094,
        _7100,
        _7103,
        _7116,
        _7126,
        _7127,
        _7128,
        _7131,
        _7132,
        _7036,
        _7091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CouplingHalfAdvancedTimeSteppingAnalysisForModulation")


class CouplingHalfAdvancedTimeSteppingAnalysisForModulation(
    _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingHalfAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingHalfAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7034.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7039.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7094.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7116.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7127.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7128.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7131.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7132.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingHalfAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2730.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingHalfAdvancedTimeSteppingAnalysisForModulation(self)
