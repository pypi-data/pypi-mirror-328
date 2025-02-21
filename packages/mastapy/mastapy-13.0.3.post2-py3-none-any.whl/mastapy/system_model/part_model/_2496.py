"""SpecialisedAssembly"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463, _2474, _2488
    from mastapy.system_model.part_model.gears import (
        _2534,
        _2536,
        _2540,
        _2542,
        _2544,
        _2546,
        _2549,
        _2552,
        _2555,
        _2557,
        _2559,
        _2561,
        _2562,
        _2564,
        _2566,
        _2568,
        _2572,
        _2574,
    )
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.part_model.couplings import (
        _2596,
        _2598,
        _2601,
        _2604,
        _2607,
        _2609,
        _2618,
        _2621,
        _2623,
        _2628,
    )
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssembly",)


Self = TypeVar("Self", bound="SpecialisedAssembly")


class SpecialisedAssembly(_2454.AbstractAssembly):
    """SpecialisedAssembly

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssembly")

    class _Cast_SpecialisedAssembly:
        """Special nested class for casting SpecialisedAssembly to subclasses."""

        def __init__(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
            parent: "SpecialisedAssembly",
        ):
            self._parent = parent

        @property
        def abstract_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2454.AbstractAssembly":
            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "SpecialisedAssembly._Cast_SpecialisedAssembly") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bolted_joint(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2463.BoltedJoint":
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.BoltedJoint)

        @property
        def flexible_pin_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2474.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.FlexiblePinAssembly)

        @property
        def agma_gleason_conical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2534.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2536.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2540.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.BevelGearSet)

        @property
        def concept_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2542.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConceptGearSet)

        @property
        def conical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2544.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.ConicalGearSet)

        @property
        def cylindrical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2546.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.CylindricalGearSet)

        @property
        def face_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2549.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.FaceGearSet)

        @property
        def gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def hypoid_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2555.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2557.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2561.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2562.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2564.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2566.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2568.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelGearSet)

        @property
        def worm_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2572.WormGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.WormGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2574.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2574

            return self._parent._cast(_2574.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2588.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.CycloidalAssembly)

        @property
        def belt_drive(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2596.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.BeltDrive)

        @property
        def clutch(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2598.Clutch":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Clutch)

        @property
        def concept_coupling(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2601.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.ConceptCoupling)

        @property
        def coupling(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2604.Coupling":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.Coupling)

        @property
        def cvt(self: "SpecialisedAssembly._Cast_SpecialisedAssembly") -> "_2607.CVT":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.CVT)

        @property
        def part_to_part_shear_coupling(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2609.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2618.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.RollingRingAssembly)

        @property
        def spring_damper(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2621.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2621

            return self._parent._cast(_2621.SpringDamper)

        @property
        def synchroniser(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2623.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2623

            return self._parent._cast(_2623.Synchroniser)

        @property
        def torque_converter(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "_2628.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.TorqueConverter)

        @property
        def specialised_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "SpecialisedAssembly":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpecialisedAssembly._Cast_SpecialisedAssembly":
        return self._Cast_SpecialisedAssembly(self)
