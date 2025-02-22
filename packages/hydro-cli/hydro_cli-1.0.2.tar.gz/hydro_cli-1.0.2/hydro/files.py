def get_wordlist(path: str):
    """
    get_wordlist attempts to create a list of words from the file at the provided path.
    """
    with open(path, errors="ignore") as f:
        return [line.strip() for line in f]


def get_hash(path: str):
    """
    get_hash attempts to retrieve the hash from the file at the provided path.
    """
    with open(path) as f:
        return f.read().strip()
