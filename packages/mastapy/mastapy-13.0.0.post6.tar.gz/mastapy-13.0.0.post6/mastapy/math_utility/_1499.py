"""CoordinateSystemEditor"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_EDITOR = python_net_import(
    "SMT.MastaAPI.MathUtility", "CoordinateSystemEditor"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1500, _1501, _1527, _1498


__docformat__ = "restructuredtext en"
__all__ = ("CoordinateSystemEditor",)


Self = TypeVar("Self", bound="CoordinateSystemEditor")


class CoordinateSystemEditor(_0.APIBase):
    """CoordinateSystemEditor

    This is a mastapy class.
    """

    TYPE = _COORDINATE_SYSTEM_EDITOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoordinateSystemEditor")

    class _Cast_CoordinateSystemEditor:
        """Special nested class for casting CoordinateSystemEditor to subclasses."""

        def __init__(
            self: "CoordinateSystemEditor._Cast_CoordinateSystemEditor",
            parent: "CoordinateSystemEditor",
        ):
            self._parent = parent

        @property
        def coordinate_system_editor(
            self: "CoordinateSystemEditor._Cast_CoordinateSystemEditor",
        ) -> "CoordinateSystemEditor":
            return self._parent

        def __getattr__(
            self: "CoordinateSystemEditor._Cast_CoordinateSystemEditor", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoordinateSystemEditor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def containing_assembly_image(self: Self) -> "Image":
        """Image"""
        temp = self.wrapped.ContainingAssemblyImage

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @containing_assembly_image.setter
    @enforce_parameter_types
    def containing_assembly_image(self: Self, value: "Image"):
        value = conversion.mp_to_pn_smt_bitmap(value)
        self.wrapped.ContainingAssemblyImage = value

    @property
    def containing_assembly_text(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContainingAssemblyText

        if temp is None:
            return ""

        return temp

    @property
    def coordinate_system_for_rotation_axes(
        self: Self,
    ) -> "_1500.CoordinateSystemForRotation":
        """mastapy.math_utility.CoordinateSystemForRotation"""
        temp = self.wrapped.CoordinateSystemForRotationAxes

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.CoordinateSystemForRotation"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1500", "CoordinateSystemForRotation"
        )(value)

    @coordinate_system_for_rotation_axes.setter
    @enforce_parameter_types
    def coordinate_system_for_rotation_axes(
        self: Self, value: "_1500.CoordinateSystemForRotation"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.CoordinateSystemForRotation"
        )
        self.wrapped.CoordinateSystemForRotationAxes = value

    @property
    def coordinate_system_for_rotation_origin(
        self: Self,
    ) -> "_1501.CoordinateSystemForRotationOrigin":
        """mastapy.math_utility.CoordinateSystemForRotationOrigin"""
        temp = self.wrapped.CoordinateSystemForRotationOrigin

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.CoordinateSystemForRotationOrigin"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1501", "CoordinateSystemForRotationOrigin"
        )(value)

    @coordinate_system_for_rotation_origin.setter
    @enforce_parameter_types
    def coordinate_system_for_rotation_origin(
        self: Self, value: "_1501.CoordinateSystemForRotationOrigin"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.CoordinateSystemForRotationOrigin"
        )
        self.wrapped.CoordinateSystemForRotationOrigin = value

    @property
    def has_modified_coordinate_system_rotation(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasModifiedCoordinateSystemRotation

        if temp is None:
            return False

        return temp

    @property
    def has_modified_coordinate_system_translation(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasModifiedCoordinateSystemTranslation

        if temp is None:
            return False

        return temp

    @property
    def has_modified_coordinate_system(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasModifiedCoordinateSystem

        if temp is None:
            return False

        return temp

    @property
    def has_rotation(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasRotation

        if temp is None:
            return False

        return temp

    @property
    def has_translation(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasTranslation

        if temp is None:
            return False

        return temp

    @property
    def root_assembly_image(self: Self) -> "Image":
        """Image"""
        temp = self.wrapped.RootAssemblyImage

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @root_assembly_image.setter
    @enforce_parameter_types
    def root_assembly_image(self: Self, value: "Image"):
        value = conversion.mp_to_pn_smt_bitmap(value)
        self.wrapped.RootAssemblyImage = value

    @property
    def root_assembly_text(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAssemblyText

        if temp is None:
            return ""

        return temp

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def rotation_axis(self: Self) -> "_1527.RotationAxis":
        """mastapy.math_utility.RotationAxis"""
        temp = self.wrapped.RotationAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.RotationAxis")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1527", "RotationAxis"
        )(value)

    @rotation_axis.setter
    @enforce_parameter_types
    def rotation_axis(self: Self, value: "_1527.RotationAxis"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.MathUtility.RotationAxis")
        self.wrapped.RotationAxis = value

    @property
    def show_preview(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowPreview

        if temp is None:
            return False

        return temp

    @show_preview.setter
    @enforce_parameter_types
    def show_preview(self: Self, value: "bool"):
        self.wrapped.ShowPreview = bool(value) if value is not None else False

    @property
    def coordinate_system(self: Self) -> "_1498.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modified_coordinate_system_for_rotation(
        self: Self,
    ) -> "_1498.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedCoordinateSystemForRotation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modified_coordinate_system_for_translation(
        self: Self,
    ) -> "_1498.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedCoordinateSystemForTranslation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotation_origin(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.RotationOrigin

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @rotation_origin.setter
    @enforce_parameter_types
    def rotation_origin(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.RotationOrigin = value

    @property
    def specified_rotation_axis(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.SpecifiedRotationAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @specified_rotation_axis.setter
    @enforce_parameter_types
    def specified_rotation_axis(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.SpecifiedRotationAxis = value

    @property
    def translation(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Translation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @translation.setter
    @enforce_parameter_types
    def translation(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Translation = value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def align_to_world_coordinate_system(self: Self):
        """Method does not return."""
        self.wrapped.AlignToWorldCoordinateSystem()

    def apply_rotation(self: Self):
        """Method does not return."""
        self.wrapped.ApplyRotation()

    def cancel_pending_changes(self: Self):
        """Method does not return."""
        self.wrapped.CancelPendingChanges()

    def set_local_origin_to_world_origin(self: Self):
        """Method does not return."""
        self.wrapped.SetLocalOriginToWorldOrigin()

    def update_origin(self: Self):
        """Method does not return."""
        self.wrapped.UpdateOrigin()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "CoordinateSystemEditor._Cast_CoordinateSystemEditor":
        return self._Cast_CoordinateSystemEditor(self)
