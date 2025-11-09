import sys
from stats import *


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_name = sys.argv[1]
    book_text = get_book_text(file_name)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    character_list = get_sorted_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in character_list:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
