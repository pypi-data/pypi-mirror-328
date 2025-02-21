"""ManufacturingMachineDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_MACHINE_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ManufacturingMachineDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("ManufacturingMachineDatabase",)


Self = TypeVar("Self", bound="ManufacturingMachineDatabase")


class ManufacturingMachineDatabase(_1846.NamedDatabase["_802.ManufacturingMachine"]):
    """ManufacturingMachineDatabase

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_MACHINE_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ManufacturingMachineDatabase")

    class _Cast_ManufacturingMachineDatabase:
        """Special nested class for casting ManufacturingMachineDatabase to subclasses."""

        def __init__(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
            parent: "ManufacturingMachineDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
        ) -> "_1846.NamedDatabase":
            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def manufacturing_machine_database(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
        ) -> "ManufacturingMachineDatabase":
            return self._parent

        def __getattr__(
            self: "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ManufacturingMachineDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ManufacturingMachineDatabase._Cast_ManufacturingMachineDatabase":
        return self._Cast_ManufacturingMachineDatabase(self)
