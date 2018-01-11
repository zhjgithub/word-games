'''
Word game.
'''


def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]


def readwordlist(filename):
    """Read the words from a file and return a set of the words
    and a set of the prefixes."""
    file = open(filename)  # opens file
    text = file.read()  # gets file into string
    wordset = set(text.upper().split())
    prefixset = set(prefix for word in wordset for prefix in prefixes(word))
    return wordset, prefixset


WORDS, PREFIXES = readwordlist('words4k.txt')


def test():
    "tests."
    assert prefixes('WORD') == ['', 'W', 'WO', 'WOR']
    assert len(WORDS) == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    print('tests pass')


if __name__ == '__main__':
    test()
