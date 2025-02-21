"""VirtualComponentAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "VirtualComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7351,
        _7352,
        _7362,
        _7363,
        _7398,
        _7298,
        _7355,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentAdvancedSystemDeflection")


class VirtualComponentAdvancedSystemDeflection(
    _7353.MountableComponentAdvancedSystemDeflection
):
    """VirtualComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentAdvancedSystemDeflection"
    )

    class _Cast_VirtualComponentAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
            parent: "VirtualComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7353.MountableComponentAdvancedSystemDeflection":
            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7298.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7355.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7351.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7352.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def point_load_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7362.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7363.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PowerLoadAdvancedSystemDeflection)

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "_7398.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
        ) -> "VirtualComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "VirtualComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection":
        return self._Cast_VirtualComponentAdvancedSystemDeflection(self)
