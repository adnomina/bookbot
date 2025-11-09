def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

        return file_contents


def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)

    return word_count


def get_character_count(book_text):
    book_text = book_text.lower()

    characters = {}

    for character in book_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters


def sort_by_num(items):
    return items["num"]


def get_sorted_list(character_count):
    character_list = []

    for char in character_count:
        if not char.isalpha():
            continue

        character_list.append({"char": char, "num": character_count[char]})

    character_list.sort(reverse=True, key=sort_by_num)

    return character_list
