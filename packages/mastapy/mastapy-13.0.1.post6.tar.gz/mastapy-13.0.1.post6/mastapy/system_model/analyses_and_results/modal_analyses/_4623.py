"""CylindricalPlanetGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4621
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CylindricalPlanetGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.system_deflections import _2750
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4636,
        _4658,
        _4597,
        _4662,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysis")


class CylindricalPlanetGearModalAnalysis(_4621.CylindricalGearModalAnalysis):
    """CylindricalPlanetGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearModalAnalysis")

    class _Cast_CylindricalPlanetGearModalAnalysis:
        """Special nested class for casting CylindricalPlanetGearModalAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
            parent: "CylindricalPlanetGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4621.CylindricalGearModalAnalysis":
            return self._parent._cast(_4621.CylindricalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4636.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4658.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4597.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_4662.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_7548.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_7545.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
        ) -> "CylindricalPlanetGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2750.CylindricalPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearModalAnalysis._Cast_CylindricalPlanetGearModalAnalysis":
        return self._Cast_CylindricalPlanetGearModalAnalysis(self)
