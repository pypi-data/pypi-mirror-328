"""__init__.py

This is the root of the mastapy package.

"""


from ._internal import (
    _MASTA_PROPERTIES,
    _MASTA_SETTERS,
    DebugEnvironment,
    MastaInitException,
    MastaPropertyException,
    MastaPropertyTypeException,
    masta_property,
    _mastafile_hook,
    masta_before,
    masta_after,
    _init_no_api_access,
    init,
    start_debugging,
    __version__,
    __api_version__,
    TupleWithName,
    CastException,
    MastapyImportException,
    overridable,
    MeasurementType,
    TypeCheckException,
    masta_licences,
)
from ._math import (
    clamp,
    sign,
    fract,
    step,
    smoothstep,
    approximately_equal,
    Long,
    Vector2D,
    Vector3D,
    Vector4D,
    Color,
    VectorException,
    Matrix2x2,
    Matrix3x3,
    Matrix4x4,
    MatrixException,
)


_mastafile_hook()


__all__ = (
    "_MASTA_PROPERTIES",
    "_MASTA_SETTERS",
    "DebugEnvironment",
    "MastaInitException",
    "MastaPropertyException",
    "MastaPropertyTypeException",
    "masta_property",
    "masta_before",
    "masta_after",
    "_init_no_api_access",
    "init",
    "start_debugging",
    "__version__",
    "__api_version__",
    "TupleWithName",
    "CastException",
    "MastapyImportException",
    "overridable",
    "MeasurementType",
    "clamp",
    "sign",
    "fract",
    "step",
    "smoothstep",
    "approximately_equal",
    "Long",
    "Vector2D",
    "Vector3D",
    "Vector4D",
    "Color",
    "VectorException",
    "Matrix2x2",
    "Matrix3x3",
    "Matrix4x4",
    "MatrixException",
    "TypeCheckException",
    "masta_licences",
)
