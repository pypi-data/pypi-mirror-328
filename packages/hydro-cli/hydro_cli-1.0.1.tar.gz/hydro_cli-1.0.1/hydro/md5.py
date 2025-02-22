import hashlib


class Cracker:
    """
    Cracker is used to find MD5 hash collisions.
    """

    def __init__(self, hash, wordlist):
        self.hash: str = hash
        self.wordlist: list[str] = wordlist

    def crack(self) -> str:
        """
        crack attempts to find a MD5 collision against the target hash
        using the provided wordlist.
        """
        for word in self.wordlist:
            if self.match_found(word):
                return word
        return ""

    def match_found(self, word: str) -> bool:
        """
        match_found checks the hash of the provided word against the target hash.
        It returns True if they match, else False.
        """
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        return hashed_word == self.hash
