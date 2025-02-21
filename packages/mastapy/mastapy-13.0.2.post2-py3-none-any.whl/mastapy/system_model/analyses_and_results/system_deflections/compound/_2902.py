"""CycloidalAssemblyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2959
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CycloidalAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2575
    from mastapy.system_model.analyses_and_results.system_deflections import _2743
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2859,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalAssemblyCompoundSystemDeflection")


class CycloidalAssemblyCompoundSystemDeflection(
    _2959.SpecialisedAssemblyCompoundSystemDeflection
):
    """CycloidalAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalAssemblyCompoundSystemDeflection"
    )

    class _Cast_CycloidalAssemblyCompoundSystemDeflection:
        """Special nested class for casting CycloidalAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
            parent: "CycloidalAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_2959.SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2959.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_2859.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
        ) -> "CycloidalAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2575.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

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
    ) -> "List[_2743.CycloidalAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection]

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
    ) -> "List[_2743.CycloidalAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection]

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
    ) -> "CycloidalAssemblyCompoundSystemDeflection._Cast_CycloidalAssemblyCompoundSystemDeflection":
        return self._Cast_CycloidalAssemblyCompoundSystemDeflection(self)
