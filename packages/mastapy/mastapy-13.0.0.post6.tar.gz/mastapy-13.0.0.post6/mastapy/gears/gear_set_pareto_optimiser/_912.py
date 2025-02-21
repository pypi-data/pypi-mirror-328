"""GearSetParetoOptimiser"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_set_pareto_optimiser import _906
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_PARETO_OPTIMISER = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "GearSetParetoOptimiser"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _950
    from mastapy.gears.gear_set_pareto_optimiser import _905, _908, _913, _938, _939


__docformat__ = "restructuredtext en"
__all__ = ("GearSetParetoOptimiser",)


Self = TypeVar("Self", bound="GearSetParetoOptimiser")


class GearSetParetoOptimiser(
    _906.DesignSpaceSearchBase[
        "_355.AbstractGearSetRating", "_911.GearSetOptimiserCandidate"
    ]
):
    """GearSetParetoOptimiser

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_PARETO_OPTIMISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetParetoOptimiser")

    class _Cast_GearSetParetoOptimiser:
        """Special nested class for casting GearSetParetoOptimiser to subclasses."""

        def __init__(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
            parent: "GearSetParetoOptimiser",
        ):
            self._parent = parent

        @property
        def design_space_search_base(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_906.DesignSpaceSearchBase":
            return self._parent._cast(_906.DesignSpaceSearchBase)

        @property
        def cylindrical_gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_905.CylindricalGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _905

            return self._parent._cast(_905.CylindricalGearSetParetoOptimiser)

        @property
        def face_gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_908.FaceGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _908

            return self._parent._cast(_908.FaceGearSetParetoOptimiser)

        @property
        def hypoid_gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_913.HypoidGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _913

            return self._parent._cast(_913.HypoidGearSetParetoOptimiser)

        @property
        def spiral_bevel_gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_938.SpiralBevelGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(_938.SpiralBevelGearSetParetoOptimiser)

        @property
        def straight_bevel_gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "_939.StraightBevelGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(_939.StraightBevelGearSetParetoOptimiser)

        @property
        def gear_set_pareto_optimiser(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser",
        ) -> "GearSetParetoOptimiser":
            return self._parent

        def __getattr__(
            self: "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetParetoOptimiser.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_designs_with_gears_which_cannot_be_manufactured_from_cutters(
        self: Self,
    ) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfDesignsWithGearsWhichCannotBeManufacturedFromCutters

        if temp is None:
            return 0

        return temp

    @property
    def remove_candidates_which_cannot_be_manufactured_with_cutters_from_database(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.RemoveCandidatesWhichCannotBeManufacturedWithCuttersFromDatabase
        )

        if temp is None:
            return False

        return temp

    @remove_candidates_which_cannot_be_manufactured_with_cutters_from_database.setter
    @enforce_parameter_types
    def remove_candidates_which_cannot_be_manufactured_with_cutters_from_database(
        self: Self, value: "bool"
    ):
        self.wrapped.RemoveCandidatesWhichCannotBeManufacturedWithCuttersFromDatabase = (
            bool(value) if value is not None else False
        )

    @property
    def remove_candidates_with_warnings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RemoveCandidatesWithWarnings

        if temp is None:
            return False

        return temp

    @remove_candidates_with_warnings.setter
    @enforce_parameter_types
    def remove_candidates_with_warnings(self: Self, value: "bool"):
        self.wrapped.RemoveCandidatesWithWarnings = (
            bool(value) if value is not None else False
        )

    @property
    def selected_candidate_geometry(self: Self) -> "_950.GearSetDesign":
        """mastapy.gears.gear_designs.GearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedCandidateGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_candidate_gear_sets(self: Self) -> "List[_950.GearSetDesign]":
        """List[mastapy.gears.gear_designs.GearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllCandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def candidate_gear_sets(self: Self) -> "List[_950.GearSetDesign]":
        """List[mastapy.gears.gear_designs.GearSetDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_chart(self: Self):
        """Method does not return."""
        self.wrapped.AddChart()

    def reset_charts(self: Self):
        """Method does not return."""
        self.wrapped.ResetCharts()

    @property
    def cast_to(self: Self) -> "GearSetParetoOptimiser._Cast_GearSetParetoOptimiser":
        return self._Cast_GearSetParetoOptimiser(self)
