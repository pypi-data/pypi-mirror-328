"""ClutchConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1534
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.static_loads import _6911, _6849
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionLoadCase",)


Self = TypeVar("Self", bound="ClutchConnectionLoadCase")


class ClutchConnectionLoadCase(_6851.CouplingConnectionLoadCase):
    """ClutchConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchConnectionLoadCase")

    class _Cast_ClutchConnectionLoadCase:
        """Special nested class for casting ClutchConnectionLoadCase to subclasses."""

        def __init__(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
            parent: "ClutchConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_connection_load_case(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_6851.CouplingConnectionLoadCase":
            return self._parent._cast(_6851.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_6911.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_6849.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_load_case(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase",
        ) -> "ClutchConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_initial_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @clutch_initial_temperature.setter
    @enforce_parameter_types
    def clutch_initial_temperature(self: Self, value: "float"):
        self.wrapped.ClutchInitialTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def clutch_pressures(self: Self) -> "_1534.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ClutchPressures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @clutch_pressures.setter
    @enforce_parameter_types
    def clutch_pressures(self: Self, value: "_1534.Vector2DListAccessor"):
        self.wrapped.ClutchPressures = value.wrapped

    @property
    def is_initially_locked(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsInitiallyLocked

        if temp is None:
            return False

        return temp

    @is_initially_locked.setter
    @enforce_parameter_types
    def is_initially_locked(self: Self, value: "bool"):
        self.wrapped.IsInitiallyLocked = bool(value) if value is not None else False

    @property
    def unlocked_clutch_linear_resistance_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UnlockedClutchLinearResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @unlocked_clutch_linear_resistance_coefficient.setter
    @enforce_parameter_types
    def unlocked_clutch_linear_resistance_coefficient(self: Self, value: "float"):
        self.wrapped.UnlockedClutchLinearResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_fixed_update_time(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseFixedUpdateTime

        if temp is None:
            return False

        return temp

    @use_fixed_update_time.setter
    @enforce_parameter_types
    def use_fixed_update_time(self: Self, value: "bool"):
        self.wrapped.UseFixedUpdateTime = bool(value) if value is not None else False

    @property
    def connection_design(self: Self) -> "_2342.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchConnectionLoadCase._Cast_ClutchConnectionLoadCase":
        return self._Cast_ClutchConnectionLoadCase(self)
