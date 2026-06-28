import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    w,g,G = np.asarray(w, dtype=float), np.asarray(g, dtype=float), np.asarray(G, dtype=float)
    G_updated = G + g**2
    w_updated = w - (lr/(np.sqrt(G_updated+eps)))*g 
    return w_updated, G_updated 