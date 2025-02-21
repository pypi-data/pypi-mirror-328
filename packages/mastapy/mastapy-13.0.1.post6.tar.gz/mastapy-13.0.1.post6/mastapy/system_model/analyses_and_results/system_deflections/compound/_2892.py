"""CVTCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CVTCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2734
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2951,
        _2851,
        _2931,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CVTCompoundSystemDeflection")


class CVTCompoundSystemDeflection(_2861.BeltDriveCompoundSystemDeflection):
    """CVTCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundSystemDeflection")

    class _Cast_CVTCompoundSystemDeflection:
        """Special nested class for casting CVTCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
            parent: "CVTCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_system_deflection(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_2861.BeltDriveCompoundSystemDeflection":
            return self._parent._cast(_2861.BeltDriveCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_2951.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_2851.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2851,
            )

            return self._parent._cast(_2851.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_2931.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_system_deflection(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
        ) -> "CVTCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_2734.CVTSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection]

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
    def assembly_analysis_cases(self: Self) -> "List[_2734.CVTSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection]

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
    ) -> "CVTCompoundSystemDeflection._Cast_CVTCompoundSystemDeflection":
        return self._Cast_CVTCompoundSystemDeflection(self)
