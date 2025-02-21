"""ElectricMachineHarmonicLoadDataFromFlux"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_FLUX = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromFlux",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6872
    from mastapy.electric_machines.harmonic_load_data import _1377, _1382, _1379


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromFlux",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromFlux")


class ElectricMachineHarmonicLoadDataFromFlux(
    _6878.ElectricMachineHarmonicLoadDataFromMotorPackages[
        "_6880.ElectricMachineHarmonicLoadFluxImportOptions"
    ]
):
    """ElectricMachineHarmonicLoadDataFromFlux

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_FLUX
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromFlux"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromFlux:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromFlux to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
            parent: "ElectricMachineHarmonicLoadDataFromFlux",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "_6878.ElectricMachineHarmonicLoadDataFromMotorPackages":
            return self._parent._cast(
                _6878.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "_6872.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "_1377.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1377

            return self._parent._cast(_1377.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "_1382.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1382

            return self._parent._cast(_1382.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "_1379.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1379

            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
        ) -> "ElectricMachineHarmonicLoadDataFromFlux":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataFromFlux.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromFlux._Cast_ElectricMachineHarmonicLoadDataFromFlux":
        return self._Cast_ElectricMachineHarmonicLoadDataFromFlux(self)
