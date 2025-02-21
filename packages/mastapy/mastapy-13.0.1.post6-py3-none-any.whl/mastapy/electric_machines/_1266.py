"""ElectricMachineSetup"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1264
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_SETUP = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineSetup"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1308, _1260


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineSetup",)


Self = TypeVar("Self", bound="ElectricMachineSetup")


class ElectricMachineSetup(_0.APIBase):
    """ElectricMachineSetup

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_SETUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineSetup")

    class _Cast_ElectricMachineSetup:
        """Special nested class for casting ElectricMachineSetup to subclasses."""

        def __init__(
            self: "ElectricMachineSetup._Cast_ElectricMachineSetup",
            parent: "ElectricMachineSetup",
        ):
            self._parent = parent

        @property
        def electric_machine_setup(
            self: "ElectricMachineSetup._Cast_ElectricMachineSetup",
        ) -> "ElectricMachineSetup":
            return self._parent

        def __getattr__(
            self: "ElectricMachineSetup._Cast_ElectricMachineSetup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineSetup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimated_material_cost(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedMaterialCost

        if temp is None:
            return 0.0

        return temp

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def number_of_air_gap_elements(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfAirGapElements

        if temp is None:
            return 0

        return temp

    @property
    def two_d_fe_model_for_electro_magnetic_analysis(
        self: Self,
    ) -> "_1308.TwoDimensionalFEModelForAnalysis[_1264.ElectricMachineMeshingOptions]":
        """mastapy.electric_machines.TwoDimensionalFEModelForAnalysis[mastapy.electric_machines.ElectricMachineMeshingOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDFEModelForElectroMagneticAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1264.ElectricMachineMeshingOptions
        ](temp)

    @property
    def eccentricity(self: Self) -> "_1260.Eccentricity":
        """mastapy.electric_machines.Eccentricity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Eccentricity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def generate_electro_magnetic_mesh(self: Self):
        """Method does not return."""
        self.wrapped.GenerateElectroMagneticMesh()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "ElectricMachineSetup._Cast_ElectricMachineSetup":
        return self._Cast_ElectricMachineSetup(self)
