"""AbstractShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2436
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.part_model import _2444, _2468
    from mastapy.system_model import _2203


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaft",)


Self = TypeVar("Self", bound="AbstractShaft")


class AbstractShaft(_2436.AbstractShaftOrHousing):
    """AbstractShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaft")

    class _Cast_AbstractShaft:
        """Special nested class for casting AbstractShaft to subclasses."""

        def __init__(
            self: "AbstractShaft._Cast_AbstractShaft", parent: "AbstractShaft"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2436.AbstractShaftOrHousing":
            return self._parent._cast(_2436.AbstractShaftOrHousing)

        @property
        def component(self: "AbstractShaft._Cast_AbstractShaft") -> "_2444.Component":
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "AbstractShaft._Cast_AbstractShaft") -> "_2468.Part":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2203.DesignEntity":
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def shaft(self: "AbstractShaft._Cast_AbstractShaft") -> "_2482.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2482

            return self._parent._cast(_2482.Shaft)

        @property
        def cycloidal_disc(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2569.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2569

            return self._parent._cast(_2569.CycloidalDisc)

        @property
        def abstract_shaft(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "AbstractShaft":
            return self._parent

        def __getattr__(self: "AbstractShaft._Cast_AbstractShaft", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaft.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AbstractShaft._Cast_AbstractShaft":
        return self._Cast_AbstractShaft(self)
