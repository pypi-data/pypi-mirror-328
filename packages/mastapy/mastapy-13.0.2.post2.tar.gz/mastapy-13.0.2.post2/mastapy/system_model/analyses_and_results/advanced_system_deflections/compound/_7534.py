"""TorqueConverterTurbineCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7453,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7404,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7491,
        _7439,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundAdvancedSystemDeflection")


class TorqueConverterTurbineCompoundAdvancedSystemDeflection(
    _7453.CouplingHalfCompoundAdvancedSystemDeflection
):
    """TorqueConverterTurbineCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    )

    class _Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
            parent: "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7453.CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7453.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
        ) -> "TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2618.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_7404.TorqueConverterTurbineAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.TorqueConverterTurbineAdvancedSystemDeflection]

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
    ) -> "List[_7404.TorqueConverterTurbineAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.TorqueConverterTurbineAdvancedSystemDeflection]

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
    ) -> "TorqueConverterTurbineCompoundAdvancedSystemDeflection._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection":
        return self._Cast_TorqueConverterTurbineCompoundAdvancedSystemDeflection(self)
