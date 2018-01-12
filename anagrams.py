'''
Anagrams.
'''

from word_game import find_words, removed


def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words
    have length >= shortest. Phrases in answer must have words in
    lexicographic order (not all permutations)."""
    return find_anagram(phrase.replace(' ', ''), shortest)


def find_anagram(letters, shortest, pre=None):
    "Using letters, from anagrams using words >= previous_word and longer than shortest."
    if pre is None:
        pre = ''
    results = set()
    for word in find_words(letters):
        if len(word) >= shortest and word >= pre:
            remainder = removed(letters, word)
            if remainder:
                for rest in find_anagram(remainder, shortest, word):
                    results.add(word + ' ' + rest)
            else:
                results.add(word)
    return results


def test():
    "tests."
    assert 'IT IT SEEN' in anagrams('ENTITIES')
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI'
    ])
    print('tests pass')


if __name__ == '__main__':
    test()
