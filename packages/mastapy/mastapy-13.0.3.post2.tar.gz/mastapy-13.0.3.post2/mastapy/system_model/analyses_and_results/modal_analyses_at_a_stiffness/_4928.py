"""CylindricalPlanetGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4926,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CylindricalPlanetGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4938,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysisAtAStiffness")


class CylindricalPlanetGearModalAnalysisAtAStiffness(
    _4926.CylindricalGearModalAnalysisAtAStiffness
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
        ) -> "_4926.CylindricalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4926.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4938.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtAStiffness._Cast_CylindricalPlanetGearModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

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
    def component_design(self: Self) -> "_2547.CylindricalPlanetGear":
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
