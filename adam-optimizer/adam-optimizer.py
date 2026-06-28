import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param, grad, m, v = np.asarray(param, dtype=float), np.asarray(grad, dtype=float), np.asarray(m, dtype=float), np.asarray(v, dtype=float)
    m_updated = beta1*m + (1-beta1)*grad 
    v_updated = beta2*v + (1-beta2)*grad**2
    m_updated_bias_correction, v_updated_bias_correction = m_updated/(1-beta1**t), v_updated/(1-beta2**t)
    param_updated = param - lr*(m_updated_bias_correction)/(np.sqrt(v_updated_bias_correction)+eps)
    return param_updated, m_updated, v_updated
    