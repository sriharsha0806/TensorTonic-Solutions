import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    # pass
    x, y = np.asarray(x), np.asarray(y)
    return np.linalg.norm(x-y)