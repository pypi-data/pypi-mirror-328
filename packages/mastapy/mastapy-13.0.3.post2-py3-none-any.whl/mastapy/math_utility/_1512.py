"""ComplexMatrix"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_MATRIX = python_net_import("SMT.MastaAPI.MathUtility", "ComplexMatrix")

if TYPE_CHECKING:
    from mastapy.math_utility import _1514, _1515, _1516


__docformat__ = "restructuredtext en"
__all__ = ("ComplexMatrix",)


Self = TypeVar("Self", bound="ComplexMatrix")


class ComplexMatrix(_1532.GenericMatrix[complex, "ComplexMatrix"]):
    """ComplexMatrix

    This is a mastapy class.
    """

    TYPE = _COMPLEX_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComplexMatrix")

    class _Cast_ComplexMatrix:
        """Special nested class for casting ComplexMatrix to subclasses."""

        def __init__(
            self: "ComplexMatrix._Cast_ComplexMatrix", parent: "ComplexMatrix"
        ):
            self._parent = parent

        @property
        def generic_matrix(
            self: "ComplexMatrix._Cast_ComplexMatrix",
        ) -> "_1532.GenericMatrix":
            pass

            return self._parent._cast(_1532.GenericMatrix)

        @property
        def complex_vector(
            self: "ComplexMatrix._Cast_ComplexMatrix",
        ) -> "_1514.ComplexVector":
            from mastapy.math_utility import _1514

            return self._parent._cast(_1514.ComplexVector)

        @property
        def complex_vector_3d(
            self: "ComplexMatrix._Cast_ComplexMatrix",
        ) -> "_1515.ComplexVector3D":
            from mastapy.math_utility import _1515

            return self._parent._cast(_1515.ComplexVector3D)

        @property
        def complex_vector_6d(
            self: "ComplexMatrix._Cast_ComplexMatrix",
        ) -> "_1516.ComplexVector6D":
            from mastapy.math_utility import _1516

            return self._parent._cast(_1516.ComplexVector6D)

        @property
        def complex_matrix(
            self: "ComplexMatrix._Cast_ComplexMatrix",
        ) -> "ComplexMatrix":
            return self._parent

        def __getattr__(self: "ComplexMatrix._Cast_ComplexMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComplexMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComplexMatrix._Cast_ComplexMatrix":
        return self._Cast_ComplexMatrix(self)
