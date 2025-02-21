"""RotorDynamicsViewable"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_DYNAMICS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "RotorDynamicsViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4026
    from mastapy.system_model.drawing import _2247, _2257, _2258


__docformat__ = "restructuredtext en"
__all__ = ("RotorDynamicsViewable",)


Self = TypeVar("Self", bound="RotorDynamicsViewable")


class RotorDynamicsViewable(_0.APIBase):
    """RotorDynamicsViewable

    This is a mastapy class.
    """

    TYPE = _ROTOR_DYNAMICS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotorDynamicsViewable")

    class _Cast_RotorDynamicsViewable:
        """Special nested class for casting RotorDynamicsViewable to subclasses."""

        def __init__(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable",
            parent: "RotorDynamicsViewable",
        ):
            self._parent = parent

        @property
        def critical_speed_analysis_viewable(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable",
        ) -> "_2247.CriticalSpeedAnalysisViewable":
            from mastapy.system_model.drawing import _2247

            return self._parent._cast(_2247.CriticalSpeedAnalysisViewable)

        @property
        def stability_analysis_viewable(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable",
        ) -> "_2257.StabilityAnalysisViewable":
            from mastapy.system_model.drawing import _2257

            return self._parent._cast(_2257.StabilityAnalysisViewable)

        @property
        def steady_state_synchronous_response_viewable(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable",
        ) -> "_2258.SteadyStateSynchronousResponseViewable":
            from mastapy.system_model.drawing import _2258

            return self._parent._cast(_2258.SteadyStateSynchronousResponseViewable)

        @property
        def rotor_dynamics_viewable(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable",
        ) -> "RotorDynamicsViewable":
            return self._parent

        def __getattr__(
            self: "RotorDynamicsViewable._Cast_RotorDynamicsViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotorDynamicsViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_dynamics(self: Self) -> "_4026.RotorDynamicsDrawStyle":
        """mastapy.system_model.analyses_and_results.rotor_dynamics.RotorDynamicsDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorDynamics

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
    def cast_to(self: Self) -> "RotorDynamicsViewable._Cast_RotorDynamicsViewable":
        return self._Cast_RotorDynamicsViewable(self)
