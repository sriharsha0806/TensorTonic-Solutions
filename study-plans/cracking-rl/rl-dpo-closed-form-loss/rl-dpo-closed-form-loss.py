import math
import numpy as np 

def sigmoid(x):
    return 1/(1+np.exp(-x))
    
def dpo_loss(log_pi_new_w, log_pi_new_l, log_pi_ref_w, log_pi_ref_l, beta):
    """
    Returns: float, DPO loss rounded to 4 decimals
    """
    # pass
    N = len(log_pi_new_w)
    Loss = 0
    for i in range(N):
        KL_loss = log_pi_new_l[i] - log_pi_ref_l[i]
        PPO_loss = log_pi_new_w[i] - log_pi_ref_w[i]
        Loss += math.log(sigmoid(beta*(PPO_loss - KL_loss)))
    return -1/N*Loss 
