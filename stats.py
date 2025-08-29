def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(texts):
    char_count = {}
    for text in texts:
        for char in text:
            if char.isalpha():
                c = char.lower()
                if c in char_count:
                    char_count[c] += 1
                else:
                    char_count[c] = 1
            else:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count
