"""BevelDifferentialGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelDifferentialGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516
    from mastapy.system_model.analyses_and_results.power_flows import _4045
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4178,
        _4179,
        _4173,
        _4201,
        _4227,
        _4265,
        _4167,
        _4246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546, _7543
    from mastapy.system_model.analyses_and_results import _2651


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetCompoundPowerFlow")


class BevelDifferentialGearSetCompoundPowerFlow(_4185.BevelGearSetCompoundPowerFlow):
    """BevelDifferentialGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetCompoundPowerFlow"
    )

    class _Cast_BevelDifferentialGearSetCompoundPowerFlow:
        """Special nested class for casting BevelDifferentialGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
            parent: "BevelDifferentialGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4185.BevelGearSetCompoundPowerFlow":
            return self._parent._cast(_4185.BevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4173.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4201.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4227.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4265.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4167.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_4246.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_7546.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_7543.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
        ) -> "BevelDifferentialGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2516.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2516.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

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
    ) -> "List[_4045.BevelDifferentialGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow]

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
    def bevel_differential_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4178.BevelDifferentialGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4179.BevelDifferentialGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4045.BevelDifferentialGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow]

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
    ) -> "BevelDifferentialGearSetCompoundPowerFlow._Cast_BevelDifferentialGearSetCompoundPowerFlow":
        return self._Cast_BevelDifferentialGearSetCompoundPowerFlow(self)
