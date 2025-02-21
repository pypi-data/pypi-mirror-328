"""TransmissionErrorToOtherPowerLoad"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_ERROR_TO_OTHER_POWER_LOAD = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TransmissionErrorToOtherPowerLoad",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1512


__docformat__ = "restructuredtext en"
__all__ = ("TransmissionErrorToOtherPowerLoad",)


Self = TypeVar("Self", bound="TransmissionErrorToOtherPowerLoad")


class TransmissionErrorToOtherPowerLoad(_0.APIBase):
    """TransmissionErrorToOtherPowerLoad

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_ERROR_TO_OTHER_POWER_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransmissionErrorToOtherPowerLoad")

    class _Cast_TransmissionErrorToOtherPowerLoad:
        """Special nested class for casting TransmissionErrorToOtherPowerLoad to subclasses."""

        def __init__(
            self: "TransmissionErrorToOtherPowerLoad._Cast_TransmissionErrorToOtherPowerLoad",
            parent: "TransmissionErrorToOtherPowerLoad",
        ):
            self._parent = parent

        @property
        def transmission_error_to_other_power_load(
            self: "TransmissionErrorToOtherPowerLoad._Cast_TransmissionErrorToOtherPowerLoad",
        ) -> "TransmissionErrorToOtherPowerLoad":
            return self._parent

        def __getattr__(
            self: "TransmissionErrorToOtherPowerLoad._Cast_TransmissionErrorToOtherPowerLoad",
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
        self: Self, instance_to_wrap: "TransmissionErrorToOtherPowerLoad.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def peak_to_peak_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def fourier_series_of_te(self: Self) -> "_1512.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FourierSeriesOfTE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TransmissionErrorToOtherPowerLoad._Cast_TransmissionErrorToOtherPowerLoad":
        return self._Cast_TransmissionErrorToOtherPowerLoad(self)
