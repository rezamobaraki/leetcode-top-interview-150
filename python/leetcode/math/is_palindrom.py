""" Last Reviewed: 2024-06-10 - Review Count: 1

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    x_str = str(x)
    last_index = len(x_str) - 1
    for num in x_str:
        if num != x_str[last_index]:
            return False
        last_index -= 1
    return True


def is_palindrome_v2(x: int) -> bool:
    if x < 0:
        return False

    if x != 0 and x % 10 == 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num


if __name__ == "__main__":
    test_cases = [121, -121, 10, 12321, 0]

    print("Version 1 (using string conversion):")
    for case in test_cases:
        result = is_palindrome_v2(case)
        print(f"is_palindrome({case}) = {result}")

    print("\nVersion 2 (without string conversion):")
    for case in test_cases:
        result = is_palindrome_v2(case)
        print(f"is_palindrome_v2({case}) = {result}")
