"""ParametricStudyVariable"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results import _2648
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_VARIABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyVariable",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4383,
        _4380,
        _4348,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyVariable",)


Self = TypeVar("Self", bound="ParametricStudyVariable")


class ParametricStudyVariable(_2648.AnalysisCaseVariable):
    """ParametricStudyVariable

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_VARIABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyVariable")

    class _Cast_ParametricStudyVariable:
        """Special nested class for casting ParametricStudyVariable to subclasses."""

        def __init__(
            self: "ParametricStudyVariable._Cast_ParametricStudyVariable",
            parent: "ParametricStudyVariable",
        ):
            self._parent = parent

        @property
        def analysis_case_variable(
            self: "ParametricStudyVariable._Cast_ParametricStudyVariable",
        ) -> "_2648.AnalysisCaseVariable":
            return self._parent._cast(_2648.AnalysisCaseVariable)

        @property
        def parametric_study_variable(
            self: "ParametricStudyVariable._Cast_ParametricStudyVariable",
        ) -> "ParametricStudyVariable":
            return self._parent

        def __getattr__(
            self: "ParametricStudyVariable._Cast_ParametricStudyVariable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyVariable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_values(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentValues

        if temp is None:
            return ""

        return temp

    @property
    def dimension(self: Self) -> "_4383.ParametricStudyDimension":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyDimension"""
        temp = self.wrapped.Dimension

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.ParametricStudyDimension",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.parametric_study_tools._4383",
            "ParametricStudyDimension",
        )(value)

    @dimension.setter
    @enforce_parameter_types
    def dimension(self: Self, value: "_4383.ParametricStudyDimension"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.ParametricStudyDimension",
        )
        self.wrapped.Dimension = value

    @property
    def distribution(self: Self) -> "_4380.MonteCarloDistribution":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.MonteCarloDistribution"""
        temp = self.wrapped.Distribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.MonteCarloDistribution",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.parametric_study_tools._4380",
            "MonteCarloDistribution",
        )(value)

    @distribution.setter
    @enforce_parameter_types
    def distribution(self: Self, value: "_4380.MonteCarloDistribution"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.MonteCarloDistribution",
        )
        self.wrapped.Distribution = value

    @property
    def end_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndValue

        if temp is None:
            return 0.0

        return temp

    @end_value.setter
    @enforce_parameter_types
    def end_value(self: Self, value: "float"):
        self.wrapped.EndValue = float(value) if value is not None else 0.0

    @property
    def group(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Group

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @group.setter
    @enforce_parameter_types
    def group(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Group = value

    @property
    def maximum_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumValue

        if temp is None:
            return 0.0

        return temp

    @maximum_value.setter
    @enforce_parameter_types
    def maximum_value(self: Self, value: "float"):
        self.wrapped.MaximumValue = float(value) if value is not None else 0.0

    @property
    def mean_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanValue

        if temp is None:
            return 0.0

        return temp

    @mean_value.setter
    @enforce_parameter_types
    def mean_value(self: Self, value: "float"):
        self.wrapped.MeanValue = float(value) if value is not None else 0.0

    @property
    def minimum_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumValue

        if temp is None:
            return 0.0

        return temp

    @minimum_value.setter
    @enforce_parameter_types
    def minimum_value(self: Self, value: "float"):
        self.wrapped.MinimumValue = float(value) if value is not None else 0.0

    @property
    def parameter_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterName

        if temp is None:
            return ""

        return temp

    @property
    def show_variable_on_axis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowVariableOnAxis

        if temp is None:
            return False

        return temp

    @show_variable_on_axis.setter
    @enforce_parameter_types
    def show_variable_on_axis(self: Self, value: "bool"):
        self.wrapped.ShowVariableOnAxis = bool(value) if value is not None else False

    @property
    def standard_deviation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StandardDeviation

        if temp is None:
            return 0.0

        return temp

    @standard_deviation.setter
    @enforce_parameter_types
    def standard_deviation(self: Self, value: "float"):
        self.wrapped.StandardDeviation = float(value) if value is not None else 0.0

    @property
    def start_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartValue

        if temp is None:
            return 0.0

        return temp

    @start_value.setter
    @enforce_parameter_types
    def start_value(self: Self, value: "float"):
        self.wrapped.StartValue = float(value) if value is not None else 0.0

    @property
    def unit(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unit

        if temp is None:
            return ""

        return temp

    @property
    def doe_variable_setter(self: Self) -> "_4348.DesignOfExperimentsVariableSetter":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.DesignOfExperimentsVariableSetter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DOEVariableSetter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def end_value_in_si_units(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @end_value_in_si_units.setter
    @enforce_parameter_types
    def end_value_in_si_units(self: Self, value: "float"):
        self.wrapped.EndValueInSIUnits = float(value) if value is not None else 0.0

    @property
    def mean_value_in_si_units(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @mean_value_in_si_units.setter
    @enforce_parameter_types
    def mean_value_in_si_units(self: Self, value: "float"):
        self.wrapped.MeanValueInSIUnits = float(value) if value is not None else 0.0

    @property
    def standard_deviation_in_si_units(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StandardDeviationInSIUnits

        if temp is None:
            return 0.0

        return temp

    @standard_deviation_in_si_units.setter
    @enforce_parameter_types
    def standard_deviation_in_si_units(self: Self, value: "float"):
        self.wrapped.StandardDeviationInSIUnits = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_value_in_si_units(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartValueInSIUnits

        if temp is None:
            return 0.0

        return temp

    @start_value_in_si_units.setter
    @enforce_parameter_types
    def start_value_in_si_units(self: Self, value: "float"):
        self.wrapped.StartValueInSIUnits = float(value) if value is not None else 0.0

    def add_to_new_group(self: Self):
        """Method does not return."""
        self.wrapped.AddToNewGroup()

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    def down(self: Self):
        """Method does not return."""
        self.wrapped.Down()

    def set_values(self: Self):
        """Method does not return."""
        self.wrapped.SetValues()

    def up(self: Self):
        """Method does not return."""
        self.wrapped.Up()

    @property
    def cast_to(self: Self) -> "ParametricStudyVariable._Cast_ParametricStudyVariable":
        return self._Cast_ParametricStudyVariable(self)
