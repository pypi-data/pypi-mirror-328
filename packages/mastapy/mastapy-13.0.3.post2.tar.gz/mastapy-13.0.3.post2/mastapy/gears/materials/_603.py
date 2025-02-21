"""KlingelnbergConicalGearMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "KlingelnbergConicalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1846, _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearMaterialDatabase",)


Self = TypeVar("Self", bound="KlingelnbergConicalGearMaterialDatabase")


class KlingelnbergConicalGearMaterialDatabase(
    _598.GearMaterialDatabase["_604.KlingelnbergCycloPalloidConicalGearMaterial"]
):
    """KlingelnbergConicalGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergConicalGearMaterialDatabase"
    )

    class _Cast_KlingelnbergConicalGearMaterialDatabase:
        """Special nested class for casting KlingelnbergConicalGearMaterialDatabase to subclasses."""

        def __init__(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
            parent: "KlingelnbergConicalGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def gear_material_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_598.GearMaterialDatabase":
            return self._parent._cast(_598.GearMaterialDatabase)

        @property
        def named_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1846.NamedDatabase":
            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def klingelnberg_conical_gear_material_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "KlingelnbergConicalGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
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
        self: Self, instance_to_wrap: "KlingelnbergConicalGearMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase":
        return self._Cast_KlingelnbergConicalGearMaterialDatabase(self)
