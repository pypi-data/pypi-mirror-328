"""CouplingHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7483,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7313,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7429,
        _7434,
        _7448,
        _7488,
        _7494,
        _7498,
        _7510,
        _7520,
        _7521,
        _7522,
        _7525,
        _7526,
        _7431,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundAdvancedSystemDeflection")


class CouplingHalfCompoundAdvancedSystemDeflection(
    _7483.MountableComponentCompoundAdvancedSystemDeflection
):
    """CouplingHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
            parent: "CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7483.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7431.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7429.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7434.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7448.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(_7448.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7488.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7494.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.PulleyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7498.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(_7498.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7510.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7520.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7521.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7522.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7525.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7526.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CouplingHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7313.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "List[_7313.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingHalfCompoundAdvancedSystemDeflection(self)
