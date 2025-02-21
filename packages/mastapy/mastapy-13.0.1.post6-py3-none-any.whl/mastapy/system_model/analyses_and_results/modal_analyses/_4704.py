"""TorqueConverterTurbineModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "TorqueConverterTurbineModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2831
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineModalAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineModalAnalysis")


class TorqueConverterTurbineModalAnalysis(_4611.CouplingHalfModalAnalysis):
    """TorqueConverterTurbineModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterTurbineModalAnalysis")

    class _Cast_TorqueConverterTurbineModalAnalysis:
        """Special nested class for casting TorqueConverterTurbineModalAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
            parent: "TorqueConverterTurbineModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_4611.CouplingHalfModalAnalysis":
            return self._parent._cast(_4611.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
        ) -> "TorqueConverterTurbineModalAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2831.TorqueConverterTurbineSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection

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
    ) -> (
        "TorqueConverterTurbineModalAnalysis._Cast_TorqueConverterTurbineModalAnalysis"
    ):
        return self._Cast_TorqueConverterTurbineModalAnalysis(self)
