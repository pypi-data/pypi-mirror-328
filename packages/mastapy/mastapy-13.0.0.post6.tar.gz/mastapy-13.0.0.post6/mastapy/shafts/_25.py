"""ShaftMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1828, _1831, _1824


__docformat__ = "restructuredtext en"
__all__ = ("ShaftMaterialDatabase",)


Self = TypeVar("Self", bound="ShaftMaterialDatabase")


class ShaftMaterialDatabase(_270.MaterialDatabase["_24.ShaftMaterial"]):
    """ShaftMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _SHAFT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftMaterialDatabase")

    class _Cast_ShaftMaterialDatabase:
        """Special nested class for casting ShaftMaterialDatabase to subclasses."""

        def __init__(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
            parent: "ShaftMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
        ) -> "_270.MaterialDatabase":
            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
        ) -> "_1828.NamedDatabase":
            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.NamedDatabase)

        @property
        def sql_database(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
        ) -> "_1831.SQLDatabase":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.SQLDatabase)

        @property
        def database(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
        ) -> "_1824.Database":
            pass

            from mastapy.utility.databases import _1824

            return self._parent._cast(_1824.Database)

        @property
        def shaft_material_database(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase",
        ) -> "ShaftMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftMaterialDatabase._Cast_ShaftMaterialDatabase":
        return self._Cast_ShaftMaterialDatabase(self)
