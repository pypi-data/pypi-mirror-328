"""ParetoFaceGearSetOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1570, _1558
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoFaceGearSetOptimisationStrategyDatabase")


class ParetoFaceGearSetOptimisationStrategyDatabase(
    _933.ParetoFaceRatingOptimisationStrategyDatabase
):
    """ParetoFaceGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoFaceGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoFaceGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
            parent: "ParetoFaceGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_933.ParetoFaceRatingOptimisationStrategyDatabase":
            return self._parent._cast(_933.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1570.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1570

            return self._parent._cast(_1570.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1558.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1558

            return self._parent._cast(_1558.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1846.NamedDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
        ) -> "ParetoFaceGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoFaceGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoFaceGearSetOptimisationStrategyDatabase._Cast_ParetoFaceGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoFaceGearSetOptimisationStrategyDatabase(self)
