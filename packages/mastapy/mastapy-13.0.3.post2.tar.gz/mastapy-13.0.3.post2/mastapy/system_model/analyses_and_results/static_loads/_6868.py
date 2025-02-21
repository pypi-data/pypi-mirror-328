"""ConicalGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.gears.gear_designs.conical import _1184, _1178
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6869,
        _6836,
        _6845,
        _6850,
        _6928,
        _6935,
        _6938,
        _6941,
        _6976,
        _6982,
        _6985,
        _7008,
        _6933,
        _6871,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshLoadCase",)


Self = TypeVar("Self", bound="ConicalGearMeshLoadCase")


class ConicalGearMeshLoadCase(_6914.GearMeshLoadCase):
    """ConicalGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshLoadCase")

    class _Cast_ConicalGearMeshLoadCase:
        """Special nested class for casting ConicalGearMeshLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
            parent: "ConicalGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6914.GearMeshLoadCase":
            return self._parent._cast(_6914.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6933.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6871.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6836.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6845.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6850.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6928.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6935

            return self._parent._cast(
                _6935.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(
                _6938.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6976.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6982.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6985.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_7008.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.ZerolBevelGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "ConicalGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Crowning = value

    @property
    def use_gleason_gems_data_for_efficiency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseGleasonGEMSDataForEfficiency

        if temp is None:
            return False

        return temp

    @use_gleason_gems_data_for_efficiency.setter
    @enforce_parameter_types
    def use_gleason_gems_data_for_efficiency(self: Self, value: "bool"):
        self.wrapped.UseGleasonGEMSDataForEfficiency = (
            bool(value) if value is not None else False
        )

    @property
    def use_ki_mo_s_data_for_efficiency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseKIMoSDataForEfficiency

        if temp is None:
            return False

        return temp

    @use_ki_mo_s_data_for_efficiency.setter
    @enforce_parameter_types
    def use_ki_mo_s_data_for_efficiency(self: Self, value: "bool"):
        self.wrapped.UseKIMoSDataForEfficiency = (
            bool(value) if value is not None else False
        )

    @property
    def use_user_specified_misalignments_in_tca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedMisalignmentsInTCA

        if temp is None:
            return False

        return temp

    @use_user_specified_misalignments_in_tca.setter
    @enforce_parameter_types
    def use_user_specified_misalignments_in_tca(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedMisalignmentsInTCA = (
            bool(value) if value is not None else False
        )

    @property
    def connection_design(self: Self) -> "_2327.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_from_imported_xml(
        self: Self,
    ) -> "_1184.KIMoSBevelHypoidSingleLoadCaseResultsData":
        """mastapy.gears.gear_designs.conical.KIMoSBevelHypoidSingleLoadCaseResultsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsFromImportedXML

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_misalignments(self: Self) -> "_1178.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedMisalignments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase]

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

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6869.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase":
        return self._Cast_ConicalGearMeshLoadCase(self)
