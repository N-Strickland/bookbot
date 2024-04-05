def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    print_report(word_count, chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def print_report(word_count, chars_dict):
    char_counts = [{"letter": key, "count": value}
                   for key, value in chars_dict.items() if key.isalpha()]
    char_counts.sort(reverse=True, key=lambda dict: dict["count"])

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document\n')

    for char_dict in char_counts:
        print(
            f"The '{char_dict['letter']}' character was found {char_dict['count']} times")

    print('\n--- End Report ---')


main()
