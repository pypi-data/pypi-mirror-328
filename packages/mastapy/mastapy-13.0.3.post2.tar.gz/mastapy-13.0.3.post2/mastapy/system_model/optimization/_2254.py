"""OptimizationStrategy"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.system_model.optimization import _2255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization", "OptimizationStrategy"
)

if TYPE_CHECKING:
    from mastapy.system_model.optimization import _2253, _2246, _2249
    from mastapy.utility.databases import _1847


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationStrategy",)


Self = TypeVar("Self", bound="OptimizationStrategy")
TStep = TypeVar("TStep", bound="_2253.OptimizationStep")


class OptimizationStrategy(_2255.OptimizationStrategyBase, Generic[TStep]):
    """OptimizationStrategy

    This is a mastapy class.

    Generic Types:
        TStep
    """

    TYPE = _OPTIMIZATION_STRATEGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationStrategy")

    class _Cast_OptimizationStrategy:
        """Special nested class for casting OptimizationStrategy to subclasses."""

        def __init__(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
            parent: "OptimizationStrategy",
        ):
            self._parent = parent

        @property
        def optimization_strategy_base(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
        ) -> "_2255.OptimizationStrategyBase":
            return self._parent._cast(_2255.OptimizationStrategyBase)

        @property
        def named_database_item(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
        ) -> "_1847.NamedDatabaseItem":
            from mastapy.utility.databases import _1847

            return self._parent._cast(_1847.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
        ) -> "_2246.ConicalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2246

            return self._parent._cast(_2246.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
        ) -> "_2249.CylindricalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2249

            return self._parent._cast(_2249.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(
            self: "OptimizationStrategy._Cast_OptimizationStrategy",
        ) -> "OptimizationStrategy":
            return self._parent

        def __getattr__(
            self: "OptimizationStrategy._Cast_OptimizationStrategy", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationStrategy.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OptimizationStrategy._Cast_OptimizationStrategy":
        return self._Cast_OptimizationStrategy(self)
