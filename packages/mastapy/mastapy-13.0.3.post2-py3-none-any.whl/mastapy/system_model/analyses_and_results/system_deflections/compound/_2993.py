"""TorqueConverterPumpCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "TorqueConverterPumpCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.system_deflections import _2850
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundSystemDeflection")


class TorqueConverterPumpCompoundSystemDeflection(
    _2911.CouplingHalfCompoundSystemDeflection
):
    """TorqueConverterPumpCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundSystemDeflection"
    )

    class _Cast_TorqueConverterPumpCompoundSystemDeflection:
        """Special nested class for casting TorqueConverterPumpCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
            parent: "TorqueConverterPumpCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_2911.CouplingHalfCompoundSystemDeflection":
            return self._parent._cast(_2911.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
        ) -> "TorqueConverterPumpCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2850.TorqueConverterPumpSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2850.TorqueConverterPumpSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpCompoundSystemDeflection._Cast_TorqueConverterPumpCompoundSystemDeflection":
        return self._Cast_TorqueConverterPumpCompoundSystemDeflection(self)
