"""PointLoadInputOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2471
from mastapy.utility_gui import _1847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "PointLoadInputOptions",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1491
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _6989,
        _6993,
        _6996,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadInputOptions",)


Self = TypeVar("Self", bound="PointLoadInputOptions")


class PointLoadInputOptions(_1847.ColumnInputOptions):
    """PointLoadInputOptions

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadInputOptions")

    class _Cast_PointLoadInputOptions:
        """Special nested class for casting PointLoadInputOptions to subclasses."""

        def __init__(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions",
            parent: "PointLoadInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions",
        ) -> "_1847.ColumnInputOptions":
            return self._parent._cast(_1847.ColumnInputOptions)

        @property
        def force_input_options(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions",
        ) -> "_6993.ForceInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6993,
            )

            return self._parent._cast(_6993.ForceInputOptions)

        @property
        def moment_input_options(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions",
        ) -> "_6996.MomentInputOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _6996,
            )

            return self._parent._cast(_6996.MomentInputOptions)

        @property
        def point_load_input_options(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions",
        ) -> "PointLoadInputOptions":
            return self._parent

        def __getattr__(
            self: "PointLoadInputOptions._Cast_PointLoadInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self: Self) -> "_1491.Axis":
        """mastapy.math_utility.Axis"""
        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.Axis")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.math_utility._1491", "Axis")(value)

    @axis.setter
    @enforce_parameter_types
    def axis(self: Self, value: "_1491.Axis"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.MathUtility.Axis")
        self.wrapped.Axis = value

    @property
    def conversion_to_load_case(self: Self) -> "_6989.AdditionalForcesObtainedFrom":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.AdditionalForcesObtainedFrom"""
        temp = self.wrapped.ConversionToLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.AdditionalForcesObtainedFrom",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition._6989",
            "AdditionalForcesObtainedFrom",
        )(value)

    @conversion_to_load_case.setter
    @enforce_parameter_types
    def conversion_to_load_case(
        self: Self, value: "_6989.AdditionalForcesObtainedFrom"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.AdditionalForcesObtainedFrom",
        )
        self.wrapped.ConversionToLoadCase = value

    @property
    def point_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PointLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PointLoad]"""
        temp = self.wrapped.PointLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PointLoad",
        )(temp)

    @point_load.setter
    @enforce_parameter_types
    def point_load(self: Self, value: "_2471.PointLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PointLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PointLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.PointLoad = value

    @property
    def cast_to(self: Self) -> "PointLoadInputOptions._Cast_PointLoadInputOptions":
        return self._Cast_PointLoadInputOptions(self)
