"""PartToPartShearCouplingCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7443,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7356,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7504,
        _7406,
        _7485,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundAdvancedSystemDeflection")


class PartToPartShearCouplingCompoundAdvancedSystemDeflection(
    _7443.CouplingCompoundAdvancedSystemDeflection
):
    """PartToPartShearCouplingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    )

    class _Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
            parent: "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_advanced_system_deflection(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7443.CouplingCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7443.CouplingCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7406.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7485.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
        ) -> "PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7356.PartToPartShearCouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartToPartShearCouplingAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7356.PartToPartShearCouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartToPartShearCouplingAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCompoundAdvancedSystemDeflection._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection":
        return self._Cast_PartToPartShearCouplingCompoundAdvancedSystemDeflection(self)
