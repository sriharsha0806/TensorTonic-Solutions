def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    res = []
    for value in values:
        temp = []
        for i in range(degree+1):
            temp.append(value**i)
        res.append(temp)
    return res
        