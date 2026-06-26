import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x, q = np.asarray(x), np.asarray(q)
    return np.percentile(x, q, method='linear')