# 28. Find the Index of the First Occurrence in a String
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)

    if m == 0:
        return 0

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"

    print(strStr(haystack, needle))  # Output: 0

    haystack = "leetcode"
    needle = "leeto"

    print(strStr(haystack, needle))  # Output: -1