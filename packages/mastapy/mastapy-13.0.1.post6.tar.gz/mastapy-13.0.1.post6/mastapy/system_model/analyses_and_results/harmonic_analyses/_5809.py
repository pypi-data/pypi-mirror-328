"""SingleNodePeriodicExcitationWithReferenceShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SingleNodePeriodicExcitationWithReferenceShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5759,
        _5835,
        _5679,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SingleNodePeriodicExcitationWithReferenceShaft",)


Self = TypeVar("Self", bound="SingleNodePeriodicExcitationWithReferenceShaft")


class SingleNodePeriodicExcitationWithReferenceShaft(
    _5792.PeriodicExcitationWithReferenceShaft
):
    """SingleNodePeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SingleNodePeriodicExcitationWithReferenceShaft"
    )

    class _Cast_SingleNodePeriodicExcitationWithReferenceShaft:
        """Special nested class for casting SingleNodePeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
            parent: "SingleNodePeriodicExcitationWithReferenceShaft",
        ):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5792.PeriodicExcitationWithReferenceShaft":
            return self._parent._cast(_5792.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5679.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AbstractPeriodicExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5759.GeneralPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(_5759.GeneralPeriodicExcitationDetail)

        @property
        def unbalanced_mass_excitation_detail(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "_5835.UnbalancedMassExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.UnbalancedMassExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
        ) -> "SingleNodePeriodicExcitationWithReferenceShaft":
            return self._parent

        def __getattr__(
            self: "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft",
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
        self: Self,
        instance_to_wrap: "SingleNodePeriodicExcitationWithReferenceShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft":
        return self._Cast_SingleNodePeriodicExcitationWithReferenceShaft(self)
