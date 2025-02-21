"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1819 import BearingForceArrowOption
    from ._1820 import TableAndChartOptions
    from ._1821 import ThreeDViewContourOption
    from ._1822 import ThreeDViewContourOptionFirstSelection
    from ._1823 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1819": ["BearingForceArrowOption"],
        "_1820": ["TableAndChartOptions"],
        "_1821": ["ThreeDViewContourOption"],
        "_1822": ["ThreeDViewContourOptionFirstSelection"],
        "_1823": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
