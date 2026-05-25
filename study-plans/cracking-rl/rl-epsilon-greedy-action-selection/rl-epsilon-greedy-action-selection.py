def epsilon_greedy_probs(Q_values, epsilon):
    """
    Returns: list of length A, action probabilities under epsilon-greedy, rounded to 4 decimals
    """
    # pass
    A = len(Q_values)
    max_a = max(Q_values)
    a1 = Q_values.index(max_a)
    vals= []
    for i, ele in enumerate(Q_values):
        val = (1-epsilon) + epsilon/A if i == a1 else epsilon/A 
        vals.append(val)
    return vals
