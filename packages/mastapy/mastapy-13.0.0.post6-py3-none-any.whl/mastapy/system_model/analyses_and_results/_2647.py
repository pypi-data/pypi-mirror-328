"""TorsionalSystemDeflectionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "TorsionalSystemDeflectionAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7552


__docformat__ = "restructuredtext en"
__all__ = ("TorsionalSystemDeflectionAnalysis",)


Self = TypeVar("Self", bound="TorsionalSystemDeflectionAnalysis")


class TorsionalSystemDeflectionAnalysis(_2620.SingleAnalysis):
    """TorsionalSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorsionalSystemDeflectionAnalysis")

    class _Cast_TorsionalSystemDeflectionAnalysis:
        """Special nested class for casting TorsionalSystemDeflectionAnalysis to subclasses."""

        def __init__(
            self: "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis",
            parent: "TorsionalSystemDeflectionAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis",
        ) -> "_2620.SingleAnalysis":
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis",
        ) -> "_7552.MarshalByRefObjectPermanent":
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def torsional_system_deflection_analysis(
            self: "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis",
        ) -> "TorsionalSystemDeflectionAnalysis":
            return self._parent

        def __getattr__(
            self: "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis",
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
        self: Self, instance_to_wrap: "TorsionalSystemDeflectionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorsionalSystemDeflectionAnalysis._Cast_TorsionalSystemDeflectionAnalysis":
        return self._Cast_TorsionalSystemDeflectionAnalysis(self)
