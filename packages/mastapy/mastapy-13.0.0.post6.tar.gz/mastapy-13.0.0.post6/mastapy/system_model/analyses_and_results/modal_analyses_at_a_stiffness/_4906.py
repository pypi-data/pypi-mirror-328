"""CylindricalPlanetGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4904,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CylindricalPlanetGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4916,
        _4935,
        _4881,
        _4937,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7544
    from mastapy.system_model.analyses_and_results import _2657, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysisAtAStiffness")


class CylindricalPlanetGearModalAnalysisAtAStiffness(
    _4904.CylindricalGearModalAnalysisAtAStiffness
):
    """CylindricalPlanetGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearModalAnalysisAtAStiffness"
    )

    class _Cast_CylindricalPlanetGearModalAnalysisAtAStiffness:
        """Special nested class for casting CylindricalPlanetGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
            parent: "CylindricalPlanetGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4904.CylindricalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4904.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4916.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4935.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4881.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4937.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7547.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7544.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2657.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "CylindricalPlanetGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CylindricalPlanetGearModalAnalysisAtAStiffness.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness":
        return self._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness(self)
