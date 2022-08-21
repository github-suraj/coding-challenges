'''
Generate words from random string and match with list's string
    lst = ["cat","baby","dog","giraffe","man"]
        string1 = "tbdcgaianm"
            output -> cat,man
        string2 = "bsaysad"
            output -> None
        string3 = "aobdcgt"
            output -> cat, dog
'''


def generate_words_from_random_string(wordlist, _string):
    '''
        Generate words from random string and match with list's string
    '''
    words = []
    for word in wordlist:
        _word = ''
        _string_list = list(_string)
        for char in word:
            try:
                char_idx = _string_list.index(char)
            except ValueError:
                continue
            _word += _string_list.pop(char_idx)

        if len(word) == len(_word):
            words.append(word)

    if words:
        print(f"{_string} -> {','.join(words)}")
    else:
        print(f'{_string} -> None')

    return words if words else None


if __name__ == '__main__':
    word_list = ["cat","baby","dog","giraffe","man"]
    generate_words_from_random_string(word_list, 'tbdcgaianm')
    generate_words_from_random_string(word_list, 'bsaysad')
    generate_words_from_random_string(word_list, 'aobdcgt')
