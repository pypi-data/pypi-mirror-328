"""FESubstructureType"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureType"
)


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureType",)


Self = TypeVar("Self", bound="FESubstructureType")


class FESubstructureType(Enum):
    """FESubstructureType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_SUBSTRUCTURE_TYPE

    FULL_FE_MESH = 0
    EXTERNALLY_REDUCED_FE = 1
    CREATE_SHAFT_MESH = 2
    IMPORTED_STL_MESH = 3
    GEOMETRY_FROM_GEOMETRY_MODELLER = 4
    FE_MESH_FROM_GEOMETRY_MODELLER = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FESubstructureType.__setattr__ = __enum_setattr
FESubstructureType.__delattr__ = __enum_delattr
