"""ElectricMachineResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResults"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1887
    from mastapy.electric_machines import _1279, _1284
    from mastapy.electric_machines.results import (
        _1353,
        _1345,
        _1347,
        _1349,
        _1362,
        _1363,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResults",)


Self = TypeVar("Self", bound="ElectricMachineResults")


class ElectricMachineResults(_0.APIBase):
    """ElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineResults")

    class _Cast_ElectricMachineResults:
        """Special nested class for casting ElectricMachineResults to subclasses."""

        def __init__(
            self: "ElectricMachineResults._Cast_ElectricMachineResults",
            parent: "ElectricMachineResults",
        ):
            self._parent = parent

        @property
        def on_load_electric_machine_results(
            self: "ElectricMachineResults._Cast_ElectricMachineResults",
        ) -> "_1362.OnLoadElectricMachineResults":
            from mastapy.electric_machines.results import _1362

            return self._parent._cast(_1362.OnLoadElectricMachineResults)

        @property
        def open_circuit_electric_machine_results(
            self: "ElectricMachineResults._Cast_ElectricMachineResults",
        ) -> "_1363.OpenCircuitElectricMachineResults":
            from mastapy.electric_machines.results import _1363

            return self._parent._cast(_1363.OpenCircuitElectricMachineResults)

        @property
        def electric_machine_results(
            self: "ElectricMachineResults._Cast_ElectricMachineResults",
        ) -> "ElectricMachineResults":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResults._Cast_ElectricMachineResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_d_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageDAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_q_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageQAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_torque_mst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageTorqueMST

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_rotor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EddyCurrentLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_stator_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EddyCurrentLossStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_stator_yoke(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EddyCurrentLossStatorYoke

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_stator(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EddyCurrentLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_total(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EddyCurrentLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_rotor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_stator_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessLossStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_stator_yoke(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessLossStatorYoke

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_stator(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_total(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcessLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def flux_density_in_air_gap_chart_at_time_0(
        self: Self,
    ) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluxDensityInAirGapChartAtTime0

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_density_in_air_gap_mst_chart_at_time_0(
        self: Self,
    ) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceDensityInAirGapMSTChartAtTime0

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hysteresis_loss_rotor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_stator_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_stator_yoke(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossStatorYoke

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_stator(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_total(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_rotor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossFundamentalRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_stator_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossFundamentalStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_stator_yoke(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossFundamentalStatorYoke

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_stator(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossFundamentalStator

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_rotor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossMinorLoopRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_stator_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossMinorLoopStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_stator_yoke(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossMinorLoopStatorYoke

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_stator(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HysteresisLossMinorLoopStator

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_loss_build_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ripple_mst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRippleMST

        if temp is None:
            return 0.0

        return temp

    @property
    def total_ac_winding_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalACWindingLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_core_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_magnet_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMagnetLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rotor_core_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRotorCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_stator_core_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalStatorCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_stator_teeth_iron_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalStatorTeethIronLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_stator_yoke_iron_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalStatorYokeIronLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_detail(self: Self) -> "_1279.ElectricMachineDetail":
        """mastapy.electric_machines.ElectricMachineDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def setup(self: Self) -> "_1284.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Setup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_timesteps(self: Self) -> "List[_1353.ElectricMachineResultsTimeStep]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsTimeStep]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsTimesteps

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_conductor_turns(
        self: Self,
    ) -> "List[_1345.ElectricMachineResultsForConductorTurn]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsForConductorTurn]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForConductorTurns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_line_to_line(
        self: Self,
    ) -> "List[_1347.ElectricMachineResultsForLineToLine]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsForLineToLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForLineToLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_phases(self: Self) -> "List[_1349.ElectricMachineResultsForPhase]":
        """List[mastapy.electric_machines.results.ElectricMachineResultsForPhase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForPhases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_this_and_slices(self: Self) -> "List[ElectricMachineResults]":
        """List[mastapy.electric_machines.results.ElectricMachineResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForThisAndSlices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def cast_to(self: Self) -> "ElectricMachineResults._Cast_ElectricMachineResults":
        return self._Cast_ElectricMachineResults(self)
