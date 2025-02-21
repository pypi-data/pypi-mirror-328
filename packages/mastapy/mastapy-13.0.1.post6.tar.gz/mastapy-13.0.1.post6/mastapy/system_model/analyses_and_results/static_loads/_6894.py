"""GearMeshTEOrderType"""
from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_MESH_TE_ORDER_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshTEOrderType"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshTEOrderType",)


Self = TypeVar("Self", bound="GearMeshTEOrderType")


class GearMeshTEOrderType(Enum):
    """GearMeshTEOrderType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_MESH_TE_ORDER_TYPE

    ORDERS_WITH_RESPECT_TO_PRIMARY_MESH_ORDER = 0
    ORDERS_WITH_RESPECT_TO_REFERENCE_SHAFT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearMeshTEOrderType.__setattr__ = __enum_setattr
GearMeshTEOrderType.__delattr__ = __enum_delattr
