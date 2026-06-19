import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x.sort()
    n = len(x)
    mean = sum(x)/n 
    if n%2:
        median = x[n//2]
        
    else:
        median = (x[(n-1)//2] + x[(n)//2])/2
    c = Counter(x)
    maximum = 0
    mode = 0
    for k in c.keys():
        temp = max(c[k], maximum)
        if temp > maximum:
            mode = k 
            maximum = temp 
    return mean, median, mode
    