"""ElectricMachineHarmonicLoadDataFromJMAG"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromJMAG",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6872
    from mastapy.electric_machines.harmonic_load_data import _1377, _1382, _1379


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromJMAG",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromJMAG")


class ElectricMachineHarmonicLoadDataFromJMAG(
    _6878.ElectricMachineHarmonicLoadDataFromMotorPackages[
        "_6882.ElectricMachineHarmonicLoadJMAGImportOptions"
    ]
):
    """ElectricMachineHarmonicLoadDataFromJMAG

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromJMAG"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromJMAG:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromJMAG to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
            parent: "ElectricMachineHarmonicLoadDataFromJMAG",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "_6878.ElectricMachineHarmonicLoadDataFromMotorPackages":
            return self._parent._cast(
                _6878.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "_6872.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "_1377.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1377

            return self._parent._cast(_1377.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "_1382.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1382

            return self._parent._cast(_1382.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "_1379.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1379

            return self._parent._cast(_1379.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
        ) -> "ElectricMachineHarmonicLoadDataFromJMAG":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataFromJMAG.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG":
        return self._Cast_ElectricMachineHarmonicLoadDataFromJMAG(self)
