"""FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MISALIGNMENTS_WITH_RESPECT_TO_CROSS_POINT_CALCULATOR = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
        "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    )
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1160


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",)


Self = TypeVar(
    "Self", bound="FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"
)


class FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator(_0.APIBase):
    """FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MISALIGNMENTS_WITH_RESPECT_TO_CROSS_POINT_CALCULATOR
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    )

    class _Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator:
        """Special nested class for casting FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator to subclasses."""

        def __init__(
            self: "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
            parent: "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
        ):
            self._parent = parent

        @property
        def face_gear_mesh_misalignments_with_respect_to_cross_point_calculator(
            self: "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
        ) -> "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
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
        self: Self,
        instance_to_wrap: "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignments_pinion(self: Self) -> "_1160.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_total(self: Self) -> "_1160.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_wheel(self: Self) -> "_1160.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator":
        return self._Cast_FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator(
            self
        )
