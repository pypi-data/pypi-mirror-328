"""VirtualComponentCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "VirtualComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7420,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7502,
        _7503,
        _7513,
        _7514,
        _7548,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundAdvancedSystemDeflection")


class VirtualComponentCompoundAdvancedSystemDeflection(
    _7504.MountableComponentCompoundAdvancedSystemDeflection
):
    """VirtualComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
            parent: "VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7502.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(_7502.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7503.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7513.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(_7513.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7514.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(_7514.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7548.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7548,
            )

            return self._parent._cast(
                _7548.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "VirtualComponentCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7420.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7420.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection":
        return self._Cast_VirtualComponentCompoundAdvancedSystemDeflection(self)
