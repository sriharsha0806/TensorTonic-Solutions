import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    N = len(X)
    X = np.asarray(X, dtype=float)
    if X.shape[0] < 2 or X.ndim != 2:
        return None
    mu = np.mean(X, axis=0)
    X_centered = X-mu 
    res = X_centered.T@X_centered
    return res/(N-1)