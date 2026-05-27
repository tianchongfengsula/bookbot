from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def get_total_words(string=""):
    """
    It accepts a string of words then will give the total words from it
    """
    print(f"Found {len(string.split())} total words")

def get_total_chars(string=""):
    chars = sorted(list(string.lower()))
    uniq_chars = set()
    chars_count = dict()
    # Reads the whole texts and then only shove the unique chars as the key then the dups
    # including the key will be counted as the total
    for char in chars:
        uniq_chars.add(char)
    for char in chars:
        if char in uniq_chars:
            chars_count[char] = chars_count.get(char, 0) + 1

    return chars_count

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list:
    result = []
    for char in char_counts:
        result.append({"char": char, "num": char_counts[char]})
    # sort here
    result.sort(reverse=True, key=sort_on)
    return result
