"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1449 import InterferenceFitDutyCycleRating
else:
    import_structure = {
        "_1449": ["InterferenceFitDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("InterferenceFitDutyCycleRating",)
