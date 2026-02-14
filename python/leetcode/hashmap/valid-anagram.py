"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    return s_count == t_count


def is_anagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_count = {}

    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    for char in t:
        if char not in s_count or s_count[char] == 0:
            return False
        s_count[char] -= 1
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))  # True

    s = "rat"
    t = "car"
    print(is_anagram(s, t))  # False
