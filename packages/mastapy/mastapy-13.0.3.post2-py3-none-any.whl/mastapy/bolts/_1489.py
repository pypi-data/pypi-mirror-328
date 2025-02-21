"""BoltMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bolts import _1485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Bolts", "BoltMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("BoltMaterialDatabase",)


Self = TypeVar("Self", bound="BoltMaterialDatabase")


class BoltMaterialDatabase(_1485.BoltedJointMaterialDatabase["_1488.BoltMaterial"]):
    """BoltMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BOLT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltMaterialDatabase")

    class _Cast_BoltMaterialDatabase:
        """Special nested class for casting BoltMaterialDatabase to subclasses."""

        def __init__(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
            parent: "BoltMaterialDatabase",
        ):
            self._parent = parent

        @property
        def bolted_joint_material_database(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
        ) -> "_1485.BoltedJointMaterialDatabase":
            return self._parent._cast(_1485.BoltedJointMaterialDatabase)

        @property
        def named_database(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
        ) -> "_1846.NamedDatabase":
            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def bolt_material_database(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase",
        ) -> "BoltMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BoltMaterialDatabase._Cast_BoltMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BoltMaterialDatabase._Cast_BoltMaterialDatabase":
        return self._Cast_BoltMaterialDatabase(self)
