

def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix_2(strs: list[str]) -> str:
    prefix = strs[0]
    prefix_len = len(prefix)

    for s in strs[1:]:
        while prefix != s[0:prefix_len]:
            prefix_len -= 1
            if prefix_len == 0:
                return ""

            prefix = prefix[0:prefix_len]

    return prefix


def longest_common_prefix_v3(strs: list[str]) -> str:
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]

if __name__ == '__main__':
    # print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
    # print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""

    print(longest_common_prefix_2(["flower", "flow", "flight"]))  # Output: "fl"
    print(longest_common_prefix_2(["dog", "racecar", "car"]))  # Output: ""
