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
    words_dict = {}
    all_value_sum = 0
    for word in args:
        sum = 0
        for letter in word:
            sum += ord(letter)
        words_dict[word] = sum
        all_value_sum += sum

    if all_value_sum % 2 == 0:
        sorted_result = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key = lambda x: (x[0]))]
    else:
        sorted_result = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key = lambda x: (-x[1]))]

    return "\n".join(sorted_result)

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


