"""TorqueConverterTurbineLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6925,
        _6838,
        _6929,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterTurbineLoadCase")


class TorqueConverterTurbineLoadCase(_6853.CouplingHalfLoadCase):
    """TorqueConverterTurbineLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterTurbineLoadCase")

    class _Cast_TorqueConverterTurbineLoadCase:
        """Special nested class for casting TorqueConverterTurbineLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
            parent: "TorqueConverterTurbineLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6853.CouplingHalfLoadCase":
            return self._parent._cast(_6853.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6925.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6838.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ComponentLoadCase)

        @property
        def part_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6929.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartLoadCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "TorqueConverterTurbineLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterTurbineLoadCase.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase":
        return self._Cast_TorqueConverterTurbineLoadCase(self)
