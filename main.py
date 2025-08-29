import sys
from stats import get_word_count, get_char_count, sort_by_freq

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    try:
        sys.argv[1]
    except Exception as e:
        sys.exit("Usage: python3 main.py <path_to_book>")
    book_path = sys.argv[1]
    book_texts = get_book_text(book_path)
    num_words = get_word_count(book_texts)
    char_count = get_char_count(book_texts)
    sorted_list = sort_by_freq(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_list:
        print(f"{c["char"]}: {c["freq"]}")
    print("============= END ===============")

main()
