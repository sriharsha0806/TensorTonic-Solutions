import math
import numpy as np 

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
def bradley_terry_loss(r_chosen, r_rejected):
    """
    Returns: float, Bradley-Terry preference loss rounded to 4 decimals
    """
    # pass
    N = len(r_chosen)
    Loss = 0
    for i in range(N):
        Loss += math.log(sigmoid(r_chosen[i]-r_rejected[i]))
    return -1/N*Loss 
        
