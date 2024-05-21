# count the frequency of each letter that appearance in a string


def letter_frequency_counter(string):
    letter_0 = {}
    for letter in string:
        if letter():
            letter_frequency_counter[letter] += 1
        else:
            letter_frequency_counter[letter] = 1
    return letter_frequency_counter
