import re


def first_repeated_word(string):
    text_no_symbols = re.sub(r'[^\w]', ' ', string)
    text_one_space = re.sub('\\s+', ' ', text_no_symbols)
    text_lower = text_one_space.lower()
    text_list = text_lower.split(" ")
    helper_list = []

    for word in text_list:
        if word in helper_list:
            return word
        else:
            helper_list.append(word)
