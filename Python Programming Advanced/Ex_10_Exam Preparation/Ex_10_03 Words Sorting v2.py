"""
Test Code	                    Output	                        Comment
print(                          charm - 523                     All of the ascii values of the 'escape' word are:
    words_sorting(              escape - 625                    e = 101, s = 115, c = 99, a = 97, p = 112, e = 101
        'escape',               mythology - 1004                Their sum is 625.
        'charm',                                                We add it in the dictionary {'escape': 625}.
        'mythology'                                             The ascii values of the 'charm' are:
  ))	                                                        c = 99, h = 104, a = 97, r = 117, m = 109
                                                                Their sum is 523.
                                                                We add it in the dictionary {'escape': 625, 'charm': 625}
                                                                The ascii values of the 'mythology' word are:
                                                                m = 109, y = 121, t = 116, h = 104, o = 111, l = 108, o = 111, g = 103, y = 121.
                                                                Their sum is 1004.
                                                                We add it in the dictionary
                                                                {'escape': 625, 'charm': 523, 'mythology': 1004}
                                                                When we sum 625 + 523 + 1004 = 2152. The result is even, and we sort the dictionary
                                                                by keys in ascending order.
"""
def words_sorting(*args):
    def calculate_word_value(word):
        return sum(ord(x) for x in word)

    words_dict = {word: calculate_word_value(word) for word in args}

    total_words_value = sum(words_dict.values())
    if total_words_value % 2 == 0:
        result = sorted(words_dict.items())
    else:
        result = sorted(words_dict.items(), key=lambda p: p[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print('''charm - 523
escape - 625
mythology - 1004
''')
print('-' * 50)
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print('''escape - 625
charm - 523
eye - 323
''')
print('-' * 50)
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))

print('''accolade - 812
cacophony - 964
''')

print('-' * 50)


