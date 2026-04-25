import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    # pass
    x = np.asarray(x, dtype=float)
    return np.maximum(0,x)