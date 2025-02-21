"""BeltDriveLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltDriveLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6877,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveLoadCase",)


Self = TypeVar("Self", bound="BeltDriveLoadCase")


class BeltDriveLoadCase(_6974.SpecialisedAssemblyLoadCase):
    """BeltDriveLoadCase

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveLoadCase")

    class _Cast_BeltDriveLoadCase:
        """Special nested class for casting BeltDriveLoadCase to subclasses."""

        def __init__(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
            parent: "BeltDriveLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_load_case(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "_6877.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(_6877.CVTLoadCase)

        @property
        def belt_drive_load_case(
            self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase",
        ) -> "BeltDriveLoadCase":
            return self._parent

        def __getattr__(self: "BeltDriveLoadCase._Cast_BeltDriveLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pre_tension(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PreTension

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pre_tension.setter
    @enforce_parameter_types
    def pre_tension(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PreTension = value

    @property
    def assembly_design(self: Self) -> "_2596.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BeltDriveLoadCase._Cast_BeltDriveLoadCase":
        return self._Cast_BeltDriveLoadCase(self)
