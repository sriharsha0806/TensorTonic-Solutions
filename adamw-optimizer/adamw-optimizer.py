import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    w, m, v, grad = np.asarray(w), np.asarray(m), np.asarray(v), np.asarray(grad)
    m_updated = beta1*m + (1-beta1)*grad 
    v_updated = beta2*v + (1-beta2)*grad**2 
    w_updated = w - lr*(weight_decay*w) - lr*(m_updated)/(np.sqrt(v_updated)+eps)
    return w_updated, m_updated, v_updated