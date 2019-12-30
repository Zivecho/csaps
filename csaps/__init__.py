# -*- coding: utf-8 -*-

"""
Cubic spline approximation (smoothing)

"""

from csaps._version import __version__  # noqa

from csaps._base import (
    SplinePPFormBase,
    ISmoothingSpline,
)
from csaps._sspumv import (
    SplinePPForm,
    UnivariateCubicSmoothingSpline,
    MultivariateCubicSmoothingSpline,
)
from csaps._sspndg import (
    NdGridSplinePPForm,
    NdGridCubicSmoothingSpline,
)
from csaps._types import (
    UnivariateDataType,
    UnivariateVectorizedDataType,
    MultivariateDataType,
    NdGridDataType,
)

__all__ = [
    'SplinePPFormBase',
    'ISmoothingSpline',
    'SplinePPForm',
    'NdGridSplinePPForm',
    'UnivariateCubicSmoothingSpline',
    'MultivariateCubicSmoothingSpline',
    'NdGridCubicSmoothingSpline',

    # Type-hints
    'UnivariateDataType',
    'UnivariateVectorizedDataType',
    'MultivariateDataType',
    'NdGridDataType',
]
