"""AbstractSystemDeflectionViewable"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "AbstractSystemDeflectionViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2266, _2264, _2280
    from mastapy.system_model.analyses_and_results.system_deflections import _2847


__docformat__ = "restructuredtext en"
__all__ = ("AbstractSystemDeflectionViewable",)


Self = TypeVar("Self", bound="AbstractSystemDeflectionViewable")


class AbstractSystemDeflectionViewable(_2273.PartAnalysisCaseWithContourViewable):
    """AbstractSystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractSystemDeflectionViewable")

    class _Cast_AbstractSystemDeflectionViewable:
        """Special nested class for casting AbstractSystemDeflectionViewable to subclasses."""

        def __init__(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
            parent: "AbstractSystemDeflectionViewable",
        ):
            self._parent = parent

        @property
        def part_analysis_case_with_contour_viewable(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
        ) -> "_2273.PartAnalysisCaseWithContourViewable":
            return self._parent._cast(_2273.PartAnalysisCaseWithContourViewable)

        @property
        def advanced_system_deflection_viewable(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
        ) -> "_2264.AdvancedSystemDeflectionViewable":
            from mastapy.system_model.drawing import _2264

            return self._parent._cast(_2264.AdvancedSystemDeflectionViewable)

        @property
        def system_deflection_viewable(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
        ) -> "_2280.SystemDeflectionViewable":
            from mastapy.system_model.drawing import _2280

            return self._parent._cast(_2280.SystemDeflectionViewable)

        @property
        def abstract_system_deflection_viewable(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
        ) -> "AbstractSystemDeflectionViewable":
            return self._parent

        def __getattr__(
            self: "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractSystemDeflectionViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self: Self) -> "_2266.ContourDrawStyle":
        """mastapy.system_model.drawing.ContourDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_draw_style(self: Self) -> "_2847.SystemDeflectionDrawStyle":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflectionDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def fe_results(self: Self):
        """Method does not return."""
        self.wrapped.FEResults()

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable":
        return self._Cast_AbstractSystemDeflectionViewable(self)
