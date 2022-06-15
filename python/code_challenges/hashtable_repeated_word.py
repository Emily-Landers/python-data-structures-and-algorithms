from data_structures.hashtable import Hashtable


def first_repeated_word(txt):

    word_assesser = ""
    hash = Hashtable()

    for char in txt:
        char_lower = char.lower()
        if ord(char_lower) in range(ord("a"), ord("z")+1):
            word_assesser += char_lower
        elif len(word_assesser):
                if hash.contains(word_assesser):
                    return word_assesser
                else:
                    hash.set(word_assesser, None)
                    word_assesser = ""

    if len(word_assesser) and hash.contains(word_assesser):
        return word_assesser
    return None