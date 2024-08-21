"""
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


def word_Pattern(pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(word_Pattern(pattern, s))  # True

    pattern = "abba"
    s = "dog cat cat fish"
    print(word_Pattern(pattern, s))  # False

    pattern = "aaaa"
    s = "dog cat cat dog"
    print(word_Pattern(pattern, s))  # False
