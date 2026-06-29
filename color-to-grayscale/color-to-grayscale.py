def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    H, W, C = len(image), len(image[0]), len(image[0][0])
    gray = [[0 for _ in range(W)] for _ in range(H)] 
    for i in range(H):
        for j in range(W):
            gray[i][j] = 0.299*image[i][j][0] + 0.587*image[i][j][1] + 0.114*image[i][j][2]
    return gray