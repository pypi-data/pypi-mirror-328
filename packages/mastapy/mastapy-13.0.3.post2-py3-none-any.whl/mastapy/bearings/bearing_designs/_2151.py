"""DetailedBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs import _2154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2155,
        _2156,
        _2157,
        _2158,
        _2159,
        _2160,
        _2162,
        _2168,
        _2169,
        _2170,
        _2174,
        _2179,
        _2180,
        _2181,
        _2182,
        _2185,
        _2186,
        _2189,
        _2190,
        _2191,
        _2192,
        _2193,
        _2194,
    )
    from mastapy.bearings.bearing_designs.fluid_film import (
        _2207,
        _2209,
        _2211,
        _2213,
        _2214,
        _2215,
    )
    from mastapy.bearings.bearing_designs import _2150


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


Self = TypeVar("Self", bound="DetailedBearing")


class DetailedBearing(_2154.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE = _DETAILED_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBearing")

    class _Cast_DetailedBearing:
        """Special nested class for casting DetailedBearing to subclasses."""

        def __init__(
            self: "DetailedBearing._Cast_DetailedBearing", parent: "DetailedBearing"
        ):
            self._parent = parent

        @property
        def non_linear_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2154.NonLinearBearing":
            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2155.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2156.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2157.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2158.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2158

            return self._parent._cast(_2158.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2159.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2159

            return self._parent._cast(_2159.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2160.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2162.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2168.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2169.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2170.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2174.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2179.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2180.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2181.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2182.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2182

            return self._parent._cast(_2182.RollerBearing)

        @property
        def rolling_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2186.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2186

            return self._parent._cast(_2186.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2189.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2189

            return self._parent._cast(_2189.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2190.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2190

            return self._parent._cast(_2190.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2191.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2191

            return self._parent._cast(_2191.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2192.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2192

            return self._parent._cast(_2192.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2193.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2193

            return self._parent._cast(_2193.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2194.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2194

            return self._parent._cast(_2194.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2207.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2207

            return self._parent._cast(_2207.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2209.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2209

            return self._parent._cast(_2209.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2211.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2211

            return self._parent._cast(_2211.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2213.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2213

            return self._parent._cast(_2213.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2214.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2214

            return self._parent._cast(_2214.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2215.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2215

            return self._parent._cast(_2215.TiltingPadThrustBearing)

        @property
        def detailed_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "DetailedBearing":
            return self._parent

        def __getattr__(self: "DetailedBearing._Cast_DetailedBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DetailedBearing._Cast_DetailedBearing":
        return self._Cast_DetailedBearing(self)
