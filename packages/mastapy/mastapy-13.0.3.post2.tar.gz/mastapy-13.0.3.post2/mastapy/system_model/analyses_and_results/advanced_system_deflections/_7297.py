"""AdvancedSystemDeflectionSubAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.system_deflections import _2846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AdvancedSystemDeflectionSubAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7565,
        _7571,
        _7556,
    )
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflectionSubAnalysis",)


Self = TypeVar("Self", bound="AdvancedSystemDeflectionSubAnalysis")


class AdvancedSystemDeflectionSubAnalysis(_2846.SystemDeflection):
    """AdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdvancedSystemDeflectionSubAnalysis")

    class _Cast_AdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting AdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
            parent: "AdvancedSystemDeflectionSubAnalysis",
        ):
            self._parent = parent

        @property
        def system_deflection(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_2846.SystemDeflection":
            return self._parent._cast(_2846.SystemDeflection)

        @property
        def fe_analysis(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "AdvancedSystemDeflectionSubAnalysis":
            return self._parent

        def __getattr__(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
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
        self: Self, instance_to_wrap: "AdvancedSystemDeflectionSubAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    @enforce_parameter_types
    def current_time(self: Self, value: "float"):
        self.wrapped.CurrentTime = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis"
    ):
        return self._Cast_AdvancedSystemDeflectionSubAnalysis(self)
