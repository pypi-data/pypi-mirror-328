"""SpiralBevelGearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.SpiralBevel", "SpiralBevelGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1193
    from mastapy.gears.gear_designs.conical import _1154
    from mastapy.gears.gear_designs import _947, _948


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearDesign",)


Self = TypeVar("Self", bound="SpiralBevelGearDesign")


class SpiralBevelGearDesign(_1180.BevelGearDesign):
    """SpiralBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearDesign")

    class _Cast_SpiralBevelGearDesign:
        """Special nested class for casting SpiralBevelGearDesign to subclasses."""

        def __init__(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
            parent: "SpiralBevelGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "_1180.BevelGearDesign":
            return self._parent._cast(_1180.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "_1193.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1193

            return self._parent._cast(_1193.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "_1154.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1154

            return self._parent._cast(_1154.ConicalGearDesign)

        @property
        def gear_design(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "_947.GearDesign":
            from mastapy.gears.gear_designs import _947

            return self._parent._cast(_947.GearDesign)

        @property
        def gear_design_component(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "_948.GearDesignComponent":
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def spiral_bevel_gear_design(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign",
        ) -> "SpiralBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def recommended_maximum_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RecommendedMaximumFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SpiralBevelGearDesign._Cast_SpiralBevelGearDesign":
        return self._Cast_SpiralBevelGearDesign(self)
