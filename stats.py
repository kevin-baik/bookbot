def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(texts):
    char_count = {}
    for char in texts:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(items):
    return items["freq"]


def sort_by_freq(char_dict):
    char_list = []
    dict_keys = char_dict.keys()
    for key in dict_keys:
        if key.isalpha():
            char_list.append({"char": key, "freq": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
