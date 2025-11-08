from stats import get_book_text, get_word_count, get_character_count


def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = get_word_count(book_text)

    print(f"Found {word_count} total words")

    character_count = get_character_count(book_text)

    print(character_count)


if __name__ == "__main__":
    main()
