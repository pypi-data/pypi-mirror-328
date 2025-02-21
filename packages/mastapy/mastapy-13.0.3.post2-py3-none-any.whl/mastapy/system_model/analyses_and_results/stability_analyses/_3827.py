"""CVTStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CVTStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTStabilityAnalysis")


class CVTStabilityAnalysis(_3794.BeltDriveStabilityAnalysis):
    """CVTStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTStabilityAnalysis")

    class _Cast_CVTStabilityAnalysis:
        """Special nested class for casting CVTStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
            parent: "CVTStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_stability_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_3794.BeltDriveStabilityAnalysis":
            return self._parent._cast(_3794.BeltDriveStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis",
        ) -> "CVTStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTStabilityAnalysis._Cast_CVTStabilityAnalysis":
        return self._Cast_CVTStabilityAnalysis(self)
