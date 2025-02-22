from hydro.md5 import Cracker
from hydro.files import get_hash, get_wordlist


TEST_HASH_PATH = "tests/hash.txt"
TEST_WORDLIST_PATH = "tests/wordlist.txt"


def test_md5():
    # bad test I know, I'm too lazy to setup mocks right now, maybe down the line
    hash = get_hash(TEST_HASH_PATH)
    wordlist = get_wordlist(TEST_WORDLIST_PATH)
    cracker = Cracker(hash, wordlist)
    result = cracker.crack()
    expected = "password"
    assert result == expected
