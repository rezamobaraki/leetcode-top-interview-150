from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    magazine_dict = {}
    for char in magazine:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1
    for char in ransomNote:
        if char in magazine_dict:
            magazine_dict[char] -= 1
            if magazine_dict[char] < 0:
                return False
        else:
            return False
    return True

# magazine_dict = {}
# for char in magazine:
#     magazine_dict[char] = magazine_dict.get(char, 0) + 1
# for char in ransomNote:
#     if magazine_dict.get(char, 0) == 0:
#         return False
#     magazine_dict[char] -= 1
# return True


def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True


if __name__ == '__main__':
    print(can_construct('a', 'b'))  # False
    print(can_construct('aa', 'ab'))  # False
    print(can_construct('aa', 'aab'))  # True
    print(can_construct('aa', 'ab'))  # False
    print(can_construct('aa', 'aab'))  # True
    print(can_construct('aab', 'aab'))  # True
