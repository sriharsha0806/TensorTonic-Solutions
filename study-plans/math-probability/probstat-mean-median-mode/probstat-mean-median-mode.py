import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    # pass
    mean = np.mean(x)
    median = np.median(x)
    vals = Counter(x)
    mode = []
    great = -float('inf')
    for val in vals.values():
        if val > great:
            great = val 
    for key in vals.keys():
        if vals[key] == great:
            mode.append(key)
    
    return {
        "mean" : mean,
        "median" : median,
        "mode" : mode[0] 
    }