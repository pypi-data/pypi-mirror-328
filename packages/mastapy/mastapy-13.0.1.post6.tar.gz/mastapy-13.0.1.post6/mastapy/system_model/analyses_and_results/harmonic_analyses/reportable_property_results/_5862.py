"""HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_LOCATION_WITHIN_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5859,
        _5860,
        _5863,
        _5864,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"
)


class HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic(_0.APIBase):
    """HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_LOCATION_WITHIN_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    )

    class _Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic to subclasses."""

        def __init__(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
            parent: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_combined_for_multiple_surfaces_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ) -> "_5859.HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5859,
            )

            return self._parent._cast(
                _5859.HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_component_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ) -> "_5860.HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5860,
            )

            return self._parent._cast(
                _5860.HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_node_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ) -> "_5863.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5863,
            )

            return self._parent._cast(
                _5863.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_surface_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ) -> "_5864.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5864,
            )

            return self._parent._cast(
                _5864.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
        ) -> "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
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
        instance_to_wrap: "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic":
        return self._Cast_HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic(
            self
        )
