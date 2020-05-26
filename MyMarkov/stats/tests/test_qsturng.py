# -*- coding: utf-8 -*-
"""

Created on Wed Mar 28 13:49:11 2012

Author: Josef Perktold
"""

import numpy as np
from numpy.testing import assert_almost_equal

from statsmodels.stats.libqsturng import qsturng, psturng
from statsmodels.sandbox.stats.multicomp import get_tukeyQcrit

def test_qstrung():
    rows = [   5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,
              16,   17,   18,   19,   20,   24,   30,   40,   60,  120, 9999]
    cols = np.arange(2,11)

    for alpha in [0.01, 0.05]:
        for k in cols:
            c1 = get_tukeyQcrit(k, rows, alpha=alpha)
            c2 = qsturng(1-alpha, k, rows)
            assert_almost_equal(c1, c2, decimal=2)
            #roundtrip
            assert_almost_equal(psturng(qsturng(1-alpha, k, rows), k, rows), alpha, 5)
