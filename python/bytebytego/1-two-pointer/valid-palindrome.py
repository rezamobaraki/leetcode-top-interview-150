def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_v2(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))
    s = "race a car"
    print(is_palindrome(s))

