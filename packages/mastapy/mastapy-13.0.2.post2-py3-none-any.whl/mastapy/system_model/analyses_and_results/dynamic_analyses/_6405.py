"""TorqueConverterDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "TorqueConverterDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2615
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6385,
        _6285,
        _6366,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterDynamicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterDynamicAnalysis")


class TorqueConverterDynamicAnalysis(_6323.CouplingDynamicAnalysis):
    """TorqueConverterDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterDynamicAnalysis")

    class _Cast_TorqueConverterDynamicAnalysis:
        """Special nested class for casting TorqueConverterDynamicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
            parent: "TorqueConverterDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_dynamic_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_6323.CouplingDynamicAnalysis":
            return self._parent._cast(_6323.CouplingDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
        ) -> "TorqueConverterDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2615.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6982.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterDynamicAnalysis._Cast_TorqueConverterDynamicAnalysis":
        return self._Cast_TorqueConverterDynamicAnalysis(self)
