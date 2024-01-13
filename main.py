def word_counter(text: str) -> int:
    return len(text.split())


def get_book_contents(path: str) -> str:
    with open('books/frankenstein.txt') as f:
        book_contents = f.read()
    return book_contents


def letter_counter(text: str) -> dict:
    letter_dict = {}
    for letter in text.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_on(d: dict) -> int:
    return d["total"]


def normalize_letter_stats(input_dict: dict) -> []:
    normalized_stats = []
    for k, v in input_dict.items():
        if k.isalpha():
            normalized_stats.append({'char': k, 'total': v})
    normalized_stats.sort(reverse=True, key=sort_on)
    return normalized_stats


def print_report(book_path: str, total_words: int, letter_stats: list) -> None:
    print(f'--- Begin report of {book_path} ---')
    print(f'{total_words} words found in the document')
    print()
    for letter in letter_stats:
        print(f"The '{letter.get('char')}' character was found {letter.get('total')} times")
    print('--- End report ---')


def main():
    book_path = 'books/frankenstein.txt'
    book_contents = get_book_contents(book_path)
    total_words = word_counter(book_contents)
    letter_stats_dict = letter_counter(book_contents)
    normalized_letter_stats_list = normalize_letter_stats(letter_stats_dict)
    print_report(book_path, total_words, normalized_letter_stats_list)


if __name__ == '__main__':
    main()
