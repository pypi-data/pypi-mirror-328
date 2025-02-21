"""FEEntityGroupInteger"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_INTEGER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEEntityGroupInteger"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _181, _200
    from mastapy.nodal_analysis.component_mode_synthesis import _227


__docformat__ = "restructuredtext en"
__all__ = ("FEEntityGroupInteger",)


Self = TypeVar("Self", bound="FEEntityGroupInteger")


class FEEntityGroupInteger(_182.FEEntityGroup[int]):
    """FEEntityGroupInteger

    This is a mastapy class.
    """

    TYPE = _FE_ENTITY_GROUP_INTEGER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEEntityGroupInteger")

    class _Cast_FEEntityGroupInteger:
        """Special nested class for casting FEEntityGroupInteger to subclasses."""

        def __init__(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
            parent: "FEEntityGroupInteger",
        ):
            self._parent = parent

        @property
        def fe_entity_group(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
        ) -> "_182.FEEntityGroup":
            return self._parent._cast(_182.FEEntityGroup)

        @property
        def element_group(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
        ) -> "_181.ElementGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _181

            return self._parent._cast(_181.ElementGroup)

        @property
        def node_group(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
        ) -> "_200.NodeGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _200

            return self._parent._cast(_200.NodeGroup)

        @property
        def cms_node_group(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
        ) -> "_227.CMSNodeGroup":
            from mastapy.nodal_analysis.component_mode_synthesis import _227

            return self._parent._cast(_227.CMSNodeGroup)

        @property
        def fe_entity_group_integer(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger",
        ) -> "FEEntityGroupInteger":
            return self._parent

        def __getattr__(
            self: "FEEntityGroupInteger._Cast_FEEntityGroupInteger", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEEntityGroupInteger.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FEEntityGroupInteger._Cast_FEEntityGroupInteger":
        return self._Cast_FEEntityGroupInteger(self)
