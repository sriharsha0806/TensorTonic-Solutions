import numpy as np 
import math 

def rlhf_ppo_kl_loss(log_probs_new, log_probs_old, log_probs_ref, advantages, clip_eps, kl_coef):
    """
    Returns: float, RLHF PPO loss with KL penalty rounded to 4 decimals
    """
    # pass
    N = len(log_probs_new)
    Loss = 0
    for i in range(N):
        R = np.exp(log_probs_new[i]-log_probs_old[i])
        RLHF_PPO_LOSS = min(R*advantages[i], np.clip(R, 1-clip_eps, 1+clip_eps)*advantages[i])
        KL_LOSS = kl_coef*(log_probs_new[i] - log_probs_ref[i]) 
        Loss += RLHF_PPO_LOSS - KL_LOSS
    return -1/N*Loss 