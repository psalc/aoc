from aoc import read_input
import re

def has_three_vowels(string: str) -> bool:
    """
    Determines whether a string has at least 3 occurences of any
    vowel in it ('aeiou').
    """
    from collections import Counter

    letter_counts = Counter(string)
    vowel_counts = sum([count for letter, count in letter_counts.items() if letter in "aeiou"])

    return vowel_counts >= 3

def contains_double_letters(string: str) -> bool:
    """
    Determines whether a string contains double letters (e.g. 'aa', 'bb').
    If minimum argument is provided, the string must contain at least
    that many non-overlapping pairs of double letters.
    """
    match = re.search(r"([a-z])\1", string, flags=re.IGNORECASE)
    if match:
        return True
    
    return False

def contains_bad_string(string: str) -> bool:
    """
    Returns True if the argument string contains any of the
    bad strings.
    """
    match = re.search(r"ab|cd|pq|xy", string, flags=re.IGNORECASE)
    if match:
        return True
        
    return False

def contains_pairs(string: str) -> bool:
    """
    Determines whether the string contains at least two non-overlapping pairs
    of any two letters, like 'xyxy', 'aabcdaa' (but not 'aaa').
    """
    match = re.search(r"([a-z][a-z])\w*\1", string, flags=re.IGNORECASE)
    if match:
        return True

    return False

def contains_sandwich(string: str) -> bool:
    """
    Determines whether a string contains a "sandwich" pattern, i.e.
    one letter which repeats with exactly one letter between them,
    like 'xyx', 'abcdefeghi', or 'aaa'.
    """
    match = re.search(r"([a-z])[a-z]{1}\1", string, flags=re.IGNORECASE)
    if match:
        return True

    return False

def is_nice_string(string: str, part: int = 1) -> bool:
    """
    Determines whether string is "nice" according to the rules
    for parts 1 or 2.
    """
    if part == 1:
        return (
            has_three_vowels(string)
            and contains_double_letters(string)
            and not contains_bad_string(string)
        )
    
    if part == 2:
        return (
            contains_pairs(string)
            and contains_sandwich(string)
        )

    raise Exception(part, "Part must be either 1 or 2.")

def main():
    txt = read_input(5).strip()
    strings = txt.splitlines()
    print(f"There are {sum([is_nice_string(string, 1) for string in strings])} nice strings in part 1.")
    print(f"There are {sum([is_nice_string(string, 2) for string in strings])} nice strings in part 2.")

if __name__ == "__main__":
    main()