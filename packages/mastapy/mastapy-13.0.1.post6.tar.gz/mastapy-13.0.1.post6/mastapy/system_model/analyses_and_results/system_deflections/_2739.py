"""CylindricalGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1786
    from mastapy.gears.rating.cylindrical import _458
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.system_model.analyses_and_results.static_loads import _6864
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2745,
        _2749,
        _2742,
        _2740,
        _2741,
        _2767,
        _2727,
    )
    from mastapy.nodal_analysis import _55
    from mastapy.system_model.analyses_and_results.power_flows import _4080
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2845,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7540,
        _7541,
        _7538,
    )
    from mastapy.system_model.analyses_and_results import _2649, _2653, _2651


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearMeshSystemDeflection")


class CylindricalGearMeshSystemDeflection(_2759.GearMeshSystemDeflection):
    """CylindricalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshSystemDeflection")

    class _Cast_CylindricalGearMeshSystemDeflection:
        """Special nested class for casting CylindricalGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
            parent: "CylindricalGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2759.GearMeshSystemDeflection":
            return self._parent._cast(_2759.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2727.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_7540.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_7541.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_7538.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2649.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2653.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2651.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2740.CylindricalGearMeshSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "_2741.CylindricalGearMeshSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
        ) -> "CylindricalGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_for_harmonic_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMisalignmentForHarmonicAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def average_interference_normal_to_the_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageInterferenceNormalToTheFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def average_operating_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageOperatingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_worst_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedWorstLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_backlash_due_to_tooth_expansion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInBacklashDueToToothExpansion

        if temp is None:
            return 0.0

        return temp

    @property
    def change_in_operating_backlash_due_to_thermal_effects(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChangeInOperatingBacklashDueToThermalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def chart_of_effective_change_in_operating_centre_distance(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChartOfEffectiveChangeInOperatingCentreDistance

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def chart_of_misalignment_in_transverse_line_of_action(
        self: Self,
    ) -> "_1786.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChartOfMisalignmentInTransverseLineOfAction

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def crowning_for_tilt_stiffness_gear_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrowningForTiltStiffnessGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def crowning_for_tilt_stiffness_gear_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrowningForTiltStiffnessGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def estimated_operating_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedOperatingToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_mesh_tilt_stiffness_method(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshTiltStiffnessMethod

        if temp is None:
            return ""

        return temp

    @property
    def is_in_contact(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsInContact

        if temp is None:
            return False

        return temp

    @property
    def linear_relief_for_tilt_stiffness_gear_a(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearReliefForTiltStiffnessGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_relief_for_tilt_stiffness_gear_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearReliefForTiltStiffnessGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def load_in_loa_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadInLOAFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_change_in_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumChangeInCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_change_in_centre_distance_due_to_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumChangeInCentreDistanceDueToMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_operating_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_operating_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_operating_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_change_in_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumChangeInCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_change_in_centre_distance_due_to_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumChangeInCentreDistanceDueToMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_changes_in_operating_centre_distance_due_to_misalignment(
        self: Self,
    ) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairChangesInOperatingCentreDistanceDueToMisalignment

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_transverse_separations_for_ltca(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairTransverseSeparationsForLTCA

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def pinion_torque_for_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorqueForLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_to_inactive_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SeparationToInactiveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_root_mean_square_planetary_equivalent_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedRootMeanSquarePlanetaryEquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_effective_operating_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestEffectiveOperatingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def transmission_error_including_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorIncludingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def transmission_error_no_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorNoBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_planetary_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstPlanetaryMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def rating(self: Self) -> "_458.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_458.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2309.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6864.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a(self: Self) -> "_2745.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_2745.CylindricalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignment_data(self: Self) -> "_55.CylindricalMisalignmentCalculator":
        """mastapy.nodal_analysis.CylindricalMisalignmentCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignment_data_left_flank(
        self: Self,
    ) -> "_55.CylindricalMisalignmentCalculator":
        """mastapy.nodal_analysis.CylindricalMisalignmentCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDataLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignment_data_right_flank(
        self: Self,
    ) -> "_55.CylindricalMisalignmentCalculator":
        """mastapy.nodal_analysis.CylindricalMisalignmentCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentDataRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4080.CylindricalGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CylindricalGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears(self: Self) -> "List[_2745.CylindricalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshed_gear_system_deflections(
        self: Self,
    ) -> "List[_2749.CylindricalMeshedGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalMeshedGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshedGearSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mesh_deflections_left_flank(self: Self) -> "List[_2845.MeshDeflectionResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.MeshDeflectionResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshDeflectionsLeftFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mesh_deflections_right_flank(self: Self) -> "List[_2845.MeshDeflectionResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.MeshDeflectionResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshDeflectionsRightFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set(self: Self) -> "_2742.CylindricalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearMeshSystemDeflection._Cast_CylindricalGearMeshSystemDeflection"
    ):
        return self._Cast_CylindricalGearMeshSystemDeflection(self)
