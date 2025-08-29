from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_texts = get_book_text("./books/frankenstein.txt")
    # print(book_texts)
    num_words = get_word_count(book_texts)
    print(f"{num_words} words found in the document")

    char_count = get_char_count(book_texts)
    print(char_count)

if __name__ == "__main__":
    main()
