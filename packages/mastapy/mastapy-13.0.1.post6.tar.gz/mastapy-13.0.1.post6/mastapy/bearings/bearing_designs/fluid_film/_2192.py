"""PlainJournalHousing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_JOURNAL_HOUSING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PlainJournalHousing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1943
    from mastapy.bearings.bearing_designs.fluid_film import _2185, _2186, _2188


__docformat__ = "restructuredtext en"
__all__ = ("PlainJournalHousing",)


Self = TypeVar("Self", bound="PlainJournalHousing")


class PlainJournalHousing(_0.APIBase):
    """PlainJournalHousing

    This is a mastapy class.
    """

    TYPE = _PLAIN_JOURNAL_HOUSING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlainJournalHousing")

    class _Cast_PlainJournalHousing:
        """Special nested class for casting PlainJournalHousing to subclasses."""

        def __init__(
            self: "PlainJournalHousing._Cast_PlainJournalHousing",
            parent: "PlainJournalHousing",
        ):
            self._parent = parent

        @property
        def cylindrical_housing_journal_bearing(
            self: "PlainJournalHousing._Cast_PlainJournalHousing",
        ) -> "_2185.CylindricalHousingJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2185

            return self._parent._cast(_2185.CylindricalHousingJournalBearing)

        @property
        def machinery_encased_journal_bearing(
            self: "PlainJournalHousing._Cast_PlainJournalHousing",
        ) -> "_2186.MachineryEncasedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2186

            return self._parent._cast(_2186.MachineryEncasedJournalBearing)

        @property
        def pedestal_journal_bearing(
            self: "PlainJournalHousing._Cast_PlainJournalHousing",
        ) -> "_2188.PedestalJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2188

            return self._parent._cast(_2188.PedestalJournalBearing)

        @property
        def plain_journal_housing(
            self: "PlainJournalHousing._Cast_PlainJournalHousing",
        ) -> "PlainJournalHousing":
            return self._parent

        def __getattr__(
            self: "PlainJournalHousing._Cast_PlainJournalHousing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlainJournalHousing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def heat_emitting_area(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeatEmittingArea

        if temp is None:
            return 0.0

        return temp

    @heat_emitting_area.setter
    @enforce_parameter_types
    def heat_emitting_area(self: Self, value: "float"):
        self.wrapped.HeatEmittingArea = float(value) if value is not None else 0.0

    @property
    def heat_emitting_area_method(self: Self) -> "_1943.DefaultOrUserInput":
        """mastapy.bearings.bearing_results.DefaultOrUserInput"""
        temp = self.wrapped.HeatEmittingAreaMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.DefaultOrUserInput"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1943", "DefaultOrUserInput"
        )(value)

    @heat_emitting_area_method.setter
    @enforce_parameter_types
    def heat_emitting_area_method(self: Self, value: "_1943.DefaultOrUserInput"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.DefaultOrUserInput"
        )
        self.wrapped.HeatEmittingAreaMethod = value

    @property
    def cast_to(self: Self) -> "PlainJournalHousing._Cast_PlainJournalHousing":
        return self._Cast_PlainJournalHousing(self)
