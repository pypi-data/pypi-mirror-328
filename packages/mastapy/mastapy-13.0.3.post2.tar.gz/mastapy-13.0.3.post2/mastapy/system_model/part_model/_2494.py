"""RootAssembly"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2453
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")

if TYPE_CHECKING:
    from mastapy.system_model import _2220, _2223
    from mastapy.geometry import _312
    from mastapy.system_model.part_model.part_groups import _2510
    from mastapy.system_model.part_model.projections import _2505
    from mastapy.system_model.part_model import _2454, _2488


__docformat__ = "restructuredtext en"
__all__ = ("RootAssembly",)


Self = TypeVar("Self", bound="RootAssembly")


class RootAssembly(_2453.Assembly):
    """RootAssembly

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssembly")

    class _Cast_RootAssembly:
        """Special nested class for casting RootAssembly to subclasses."""

        def __init__(self: "RootAssembly._Cast_RootAssembly", parent: "RootAssembly"):
            self._parent = parent

        @property
        def assembly(self: "RootAssembly._Cast_RootAssembly") -> "_2453.Assembly":
            return self._parent._cast(_2453.Assembly)

        @property
        def abstract_assembly(
            self: "RootAssembly._Cast_RootAssembly",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "RootAssembly._Cast_RootAssembly") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "RootAssembly._Cast_RootAssembly",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def root_assembly(self: "RootAssembly._Cast_RootAssembly") -> "RootAssembly":
            return self._parent

        def __getattr__(self: "RootAssembly._Cast_RootAssembly", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def model(self: Self) -> "_2220.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Model

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def packaging_limits(self: Self) -> "_312.PackagingLimits":
        """mastapy.geometry.PackagingLimits

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PackagingLimits

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parallel_part_groups(self: Self) -> "List[_2510.ParallelPartGroup]":
        """List[mastapy.system_model.part_model.part_groups.ParallelPartGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParallelPartGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def parallel_part_groups_drawing_order(
        self: Self,
    ) -> "List[_2505.SpecifiedParallelPartGroupDrawingOrder]":
        """List[mastapy.system_model.part_model.projections.SpecifiedParallelPartGroupDrawingOrder]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParallelPartGroupsDrawingOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def attempt_to_fix_all_cylindrical_gear_sets_by_changing_normal_module(self: Self):
        """Method does not return."""
        self.wrapped.AttemptToFixAllCylindricalGearSetsByChangingNormalModule()

    def attempt_to_fix_all_gear_sets(self: Self):
        """Method does not return."""
        self.wrapped.AttemptToFixAllGearSets()

    def open_fe_substructure_version_comparer(self: Self):
        """Method does not return."""
        self.wrapped.OpenFESubstructureVersionComparer()

    def set_packaging_limits_to_current_bounding_box(self: Self):
        """Method does not return."""
        self.wrapped.SetPackagingLimitsToCurrentBoundingBox()

    def set_packaging_limits_to_current_bounding_box_of_all_gears(self: Self):
        """Method does not return."""
        self.wrapped.SetPackagingLimitsToCurrentBoundingBoxOfAllGears()

    @property
    def cast_to(self: Self) -> "RootAssembly._Cast_RootAssembly":
        return self._Cast_RootAssembly(self)
