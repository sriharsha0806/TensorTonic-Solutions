def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    for word in stopwords:
        while word in tokens:
            tokens.remove(word)
    return tokens