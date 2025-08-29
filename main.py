from stats import get_word_count, get_char_count, sort_by_freq

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_texts = get_book_text("./books/frankenstein.txt")
    # print(book_texts)
    num_words = get_word_count(book_texts)
    char_count = get_char_count(book_texts)
    sorted_list = sort_by_freq(char_count)

    print(f"""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------""")
    for c in sorted_list:
        print(f"{c["char"]}: {c["freq"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
