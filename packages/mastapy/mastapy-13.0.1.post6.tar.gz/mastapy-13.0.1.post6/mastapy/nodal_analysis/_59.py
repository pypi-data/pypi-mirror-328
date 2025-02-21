"""FEMeshElementEntityOption"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FE_MESH_ELEMENT_ENTITY_OPTION = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEMeshElementEntityOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEMeshElementEntityOption",)


Self = TypeVar("Self", bound="FEMeshElementEntityOption")


class FEMeshElementEntityOption(Enum):
    """FEMeshElementEntityOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FE_MESH_ELEMENT_ENTITY_OPTION

    NONE = 0
    ALL = 1
    FREE_FACES = 2
    OUTLINE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FEMeshElementEntityOption.__setattr__ = __enum_setattr
FEMeshElementEntityOption.__delattr__ = __enum_delattr
