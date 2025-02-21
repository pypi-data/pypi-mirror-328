"""CylindricalGearSetCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5047,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4905,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5034,
        _5035,
        _5071,
        _5085,
        _4987,
        _5066,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545, _7542
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundModalAnalysisAtAStiffness")


class CylindricalGearSetCompoundModalAnalysisAtAStiffness(
    _5047.GearSetCompoundModalAnalysisAtAStiffness
):
    """CylindricalGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
            parent: "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.GearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5047.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5085.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_4987.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4987,
            )

            return self._parent._cast(
                _4987.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7542.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(
                _5071.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2526.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

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
    ) -> "List[_4905.CylindricalGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalGearSetModalAnalysisAtAStiffness]

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
    def cylindrical_gears_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5034.CylindricalGearCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.CylindricalGearCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_5035.CylindricalGearMeshCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.CylindricalGearMeshCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4905.CylindricalGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CylindricalGearSetModalAnalysisAtAStiffness]

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
    ) -> "CylindricalGearSetCompoundModalAnalysisAtAStiffness._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_CylindricalGearSetCompoundModalAnalysisAtAStiffness(self)
