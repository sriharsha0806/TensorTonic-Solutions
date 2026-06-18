import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype=float)
    if v.ndim == 1:
        return v/np.linalg.norm(v)
    elif v.ndim == 2:
        norms = np.linalg.norm(v, axis = 1, keepdims=True)
        
        return np.divide(v, norms, out=np.zeros_like(v), where=norms!=0)
