import sys
from stats import get_total_words, get_total_chars, chars_dict_to_sorted_list

# NOTETOSELF: The book_path default value is reading the readme file
# Also the with open is truly op, please remember that when opening a file using python
# You can really return a file and with the use of .read()
def get_book_text(book_path="./README.md"):
    """
    Accepts a full path with the filename to read and return the read file
    """
    with open(book_path) as f:
        return f.read()


def main():
    print(f"====== {sys.argv[1]} REPORT ======")
    if len(sys.argv) == 2:
        book = sys.argv[1]
        get_total_words(get_book_text(book))
        sorted_chars = chars_dict_to_sorted_list(get_total_chars(get_book_text(book)))
        for chars in sorted_chars:
            if not chars["char"].isalpha():
                continue
            print(f"{chars['char']}: {chars['num']}")
        print("===================================")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
