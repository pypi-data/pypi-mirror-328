"""AGMAGleasonConicalGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4911,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AGMAGleasonConicalGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4890,
        _4892,
        _4893,
        _4895,
        _4942,
        _4980,
        _4986,
        _4989,
        _4991,
        _4992,
        _5007,
        _4938,
        _4957,
        _4903,
        _4959,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysisAtAStiffness")


class AGMAGleasonConicalGearModalAnalysisAtAStiffness(
    _4911.ConicalGearModalAnalysisAtAStiffness
):
    """AGMAGleasonConicalGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness"
    )

    class _Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
            parent: "AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4911.ConicalGearModalAnalysisAtAStiffness":
            return self._parent._cast(_4911.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4938.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4957.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4903.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4959.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4890.BevelDifferentialGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(
                _4890.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(
                _4892.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4893.BevelDifferentialSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(
                _4893.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4895.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.BevelGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4942.HypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.HypoidGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4980.SpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4986.StraightBevelDiffGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4986,
            )

            return self._parent._cast(
                _4986.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4989.StraightBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4989,
            )

            return self._parent._cast(_4989.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4991.StraightBevelPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4991,
            )

            return self._parent._cast(
                _4991.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_4992.StraightBevelSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(
                _4992.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "_5007.ZerolBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5007,
            )

            return self._parent._cast(_5007.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
        ) -> "AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AGMAGleasonConicalGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness":
        return self._Cast_AGMAGleasonConicalGearModalAnalysisAtAStiffness(self)
