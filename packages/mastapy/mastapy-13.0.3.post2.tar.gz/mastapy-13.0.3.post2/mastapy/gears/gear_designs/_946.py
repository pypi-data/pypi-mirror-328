"""BevelHypoidGearRatingSettingsDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "BevelHypoidGearRatingSettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1849, _1842


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearRatingSettingsDatabase",)


Self = TypeVar("Self", bound="BevelHypoidGearRatingSettingsDatabase")


class BevelHypoidGearRatingSettingsDatabase(
    _1846.NamedDatabase["_947.BevelHypoidGearRatingSettingsItem"]
):
    """BevelHypoidGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelHypoidGearRatingSettingsDatabase"
    )

    class _Cast_BevelHypoidGearRatingSettingsDatabase:
        """Special nested class for casting BevelHypoidGearRatingSettingsDatabase to subclasses."""

        def __init__(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
            parent: "BevelHypoidGearRatingSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
        ) -> "_1846.NamedDatabase":
            return self._parent._cast(_1846.NamedDatabase)

        @property
        def sql_database(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
        ) -> "_1849.SQLDatabase":
            pass

            from mastapy.utility.databases import _1849

            return self._parent._cast(_1849.SQLDatabase)

        @property
        def database(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
        ) -> "_1842.Database":
            pass

            from mastapy.utility.databases import _1842

            return self._parent._cast(_1842.Database)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
        ) -> "BevelHypoidGearRatingSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase",
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
        self: Self, instance_to_wrap: "BevelHypoidGearRatingSettingsDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearRatingSettingsDatabase._Cast_BevelHypoidGearRatingSettingsDatabase":
        return self._Cast_BevelHypoidGearRatingSettingsDatabase(self)
