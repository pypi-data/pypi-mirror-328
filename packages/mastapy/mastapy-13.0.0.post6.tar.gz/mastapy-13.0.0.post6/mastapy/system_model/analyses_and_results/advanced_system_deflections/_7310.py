"""CouplingAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7293,
        _7298,
        _7355,
        _7377,
        _7392,
        _7269,
        _7354,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CouplingAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingAdvancedSystemDeflection")


class CouplingAdvancedSystemDeflection(
    _7373.SpecialisedAssemblyAdvancedSystemDeflection
):
    """CouplingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingAdvancedSystemDeflection")

    class _Cast_CouplingAdvancedSystemDeflection:
        """Special nested class for casting CouplingAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
            parent: "CouplingAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7373.SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7373.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7269.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7269,
            )

            return self._parent._cast(_7269.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7354.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7293.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(_7293.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7298.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ConceptCouplingAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7355.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def spring_damper_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7377.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpringDamperAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "_7392.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.TorqueConverterAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "CouplingAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection":
        return self._Cast_CouplingAdvancedSystemDeflection(self)
