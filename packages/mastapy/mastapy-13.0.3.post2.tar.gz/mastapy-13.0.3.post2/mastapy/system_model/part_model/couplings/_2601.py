"""ConceptCoupling"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2604
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _54, _82
    from mastapy.math_utility import _1553
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCoupling",)


Self = TypeVar("Self", bound="ConceptCoupling")


class ConceptCoupling(_2604.Coupling):
    """ConceptCoupling

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCoupling")

    class _Cast_ConceptCoupling:
        """Special nested class for casting ConceptCoupling to subclasses."""

        def __init__(
            self: "ConceptCoupling._Cast_ConceptCoupling", parent: "ConceptCoupling"
        ):
            self._parent = parent

        @property
        def coupling(self: "ConceptCoupling._Cast_ConceptCoupling") -> "_2604.Coupling":
            return self._parent._cast(_2604.Coupling)

        @property
        def specialised_assembly(
            self: "ConceptCoupling._Cast_ConceptCoupling",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "ConceptCoupling._Cast_ConceptCoupling",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "ConceptCoupling._Cast_ConceptCoupling") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "ConceptCoupling._Cast_ConceptCoupling",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def concept_coupling(
            self: "ConceptCoupling._Cast_ConceptCoupling",
        ) -> "ConceptCoupling":
            return self._parent

        def __getattr__(self: "ConceptCoupling._Cast_ConceptCoupling", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCoupling.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coupling_type(self: Self) -> "_54.CouplingType":
        """mastapy.nodal_analysis.CouplingType"""
        temp = self.wrapped.CouplingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.CouplingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._54", "CouplingType"
        )(value)

    @coupling_type.setter
    @enforce_parameter_types
    def coupling_type(self: Self, value: "_54.CouplingType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.CouplingType"
        )
        self.wrapped.CouplingType = value

    @property
    def default_efficiency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DefaultEfficiency

        if temp is None:
            return 0.0

        return temp

    @default_efficiency.setter
    @enforce_parameter_types
    def default_efficiency(self: Self, value: "float"):
        self.wrapped.DefaultEfficiency = float(value) if value is not None else 0.0

    @property
    def default_speed_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DefaultSpeedRatio

        if temp is None:
            return 0.0

        return temp

    @default_speed_ratio.setter
    @enforce_parameter_types
    def default_speed_ratio(self: Self, value: "float"):
        self.wrapped.DefaultSpeedRatio = float(value) if value is not None else 0.0

    @property
    def display_tilt_in_2d_drawing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DisplayTiltIn2DDrawing

        if temp is None:
            return False

        return temp

    @display_tilt_in_2d_drawing.setter
    @enforce_parameter_types
    def display_tilt_in_2d_drawing(self: Self, value: "bool"):
        self.wrapped.DisplayTiltIn2DDrawing = (
            bool(value) if value is not None else False
        )

    @property
    def efficiency_vs_speed_ratio(self: Self) -> "_1553.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.EfficiencyVsSpeedRatio

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @efficiency_vs_speed_ratio.setter
    @enforce_parameter_types
    def efficiency_vs_speed_ratio(self: Self, value: "_1553.Vector2DListAccessor"):
        self.wrapped.EfficiencyVsSpeedRatio = value.wrapped

    @property
    def half_positioning(self: Self) -> "_2603.ConceptCouplingHalfPositioning":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalfPositioning"""
        temp = self.wrapped.HalfPositioning

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.Couplings.ConceptCouplingHalfPositioning",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.couplings._2603",
            "ConceptCouplingHalfPositioning",
        )(value)

    @half_positioning.setter
    @enforce_parameter_types
    def half_positioning(self: Self, value: "_2603.ConceptCouplingHalfPositioning"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.Couplings.ConceptCouplingHalfPositioning",
        )
        self.wrapped.HalfPositioning = value

    @property
    def halves_are_coincident(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HalvesAreCoincident

        if temp is None:
            return False

        return temp

    @halves_are_coincident.setter
    @enforce_parameter_types
    def halves_are_coincident(self: Self, value: "bool"):
        self.wrapped.HalvesAreCoincident = bool(value) if value is not None else False

    @property
    def specify_efficiency_vs_speed_ratio(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyEfficiencyVsSpeedRatio

        if temp is None:
            return False

        return temp

    @specify_efficiency_vs_speed_ratio.setter
    @enforce_parameter_types
    def specify_efficiency_vs_speed_ratio(self: Self, value: "bool"):
        self.wrapped.SpecifyEfficiencyVsSpeedRatio = (
            bool(value) if value is not None else False
        )

    @property
    def specify_stiffness_matrix(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyStiffnessMatrix

        if temp is None:
            return False

        return temp

    @specify_stiffness_matrix.setter
    @enforce_parameter_types
    def specify_stiffness_matrix(self: Self, value: "bool"):
        self.wrapped.SpecifyStiffnessMatrix = (
            bool(value) if value is not None else False
        )

    @property
    def tilt_about_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltAboutX

        if temp is None:
            return 0.0

        return temp

    @tilt_about_x.setter
    @enforce_parameter_types
    def tilt_about_x(self: Self, value: "float"):
        self.wrapped.TiltAboutX = float(value) if value is not None else 0.0

    @property
    def tilt_about_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltAboutY

        if temp is None:
            return 0.0

        return temp

    @tilt_about_y.setter
    @enforce_parameter_types
    def tilt_about_y(self: Self, value: "float"):
        self.wrapped.TiltAboutY = float(value) if value is not None else 0.0

    @property
    def torsional_damping(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalDamping

        if temp is None:
            return 0.0

        return temp

    @torsional_damping.setter
    @enforce_parameter_types
    def torsional_damping(self: Self, value: "float"):
        self.wrapped.TorsionalDamping = float(value) if value is not None else 0.0

    @property
    def translational_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TranslationalStiffness

        if temp is None:
            return 0.0

        return temp

    @translational_stiffness.setter
    @enforce_parameter_types
    def translational_stiffness(self: Self, value: "float"):
        self.wrapped.TranslationalStiffness = float(value) if value is not None else 0.0

    @property
    def stiffness(self: Self) -> "_82.NodalMatrixEditorWrapperConceptCouplingStiffness":
        """mastapy.nodal_analysis.NodalMatrixEditorWrapperConceptCouplingStiffness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptCoupling._Cast_ConceptCoupling":
        return self._Cast_ConceptCoupling(self)
