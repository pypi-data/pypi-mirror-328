"""ConicalGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConicalGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7279,
        _7286,
        _7291,
        _7339,
        _7343,
        _7346,
        _7349,
        _7377,
        _7383,
        _7386,
        _7405,
        _7374,
        _7270,
        _7355,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSetAdvancedSystemDeflection")


class ConicalGearSetAdvancedSystemDeflection(_7335.GearSetAdvancedSystemDeflection):
    """ConicalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearSetAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
            parent: "ConicalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7335.GearSetAdvancedSystemDeflection":
            return self._parent._cast(_7335.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7374.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7270.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(
                _7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7286.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(
                _7286.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7291.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.BevelGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7339.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7343.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7349.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7377.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7383.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7386.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(
                _7386.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "_7405.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(_7405.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
        ) -> "ConicalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

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
    ) -> "ConicalGearSetAdvancedSystemDeflection._Cast_ConicalGearSetAdvancedSystemDeflection":
        return self._Cast_ConicalGearSetAdvancedSystemDeflection(self)
