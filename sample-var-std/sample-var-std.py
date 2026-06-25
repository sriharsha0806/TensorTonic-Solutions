import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    # pass
    N = len(x)
    x = np.asarray(x)
    mean = np.mean(x)
    squared_deviations = (x - mean) ** 2
    res = np.sum(squared_deviations)
    variance = res/(N-1)
    standard_deviation = np.sqrt(variance)
    return variance, standard_deviation