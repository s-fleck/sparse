import numpy as np
from .core import COO


def assert_eq(x, y, rtol=1.e-5, atol=1.e-8):
    assert x.shape == y.shape
    assert x.dtype == y.dtype

    if isinstance(x, COO):
        if x.sorted:
            assert is_lexsorted(x)
    if isinstance(y, COO):
        if y.sorted:
            assert is_lexsorted(y)

    if hasattr(x, 'todense'):
        xx = x.todense()
    else:
        xx = x
    if hasattr(y, 'todense'):
        yy = y.todense()
    else:
        yy = y
    assert np.allclose(xx, yy, rtol=rtol, atol=atol)


def is_lexsorted(x):
    return not x.shape or (np.diff(x.linear_loc()) > 0).all()
