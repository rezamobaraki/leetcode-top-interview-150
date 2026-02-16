# Original Implementation (Fixed) - Two-pointer with character skipping
def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# Simplified Implementation - Clean and readable approach
def is_palindrome_valid_v2(s: str) -> bool:
    """
    Simpler approach: filter first, then check
    Time: O(n), Space: O(n)
    """
    # Filter only alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())

    # Check if it reads the same forwards and backwards
    return filtered == filtered[::-1]


if __name__ == "__main__":
    """
    Valid Palindrome
    Given a string, determine if it is a palindrome, considering only alphanumeric 
    characters and ignoring cases.
    """

    test_cases = [
        ("a dog! a panic in a pagoda.", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("a", True),
        ("ab", False),
        (".,", True),  # Only non-alphanumeric, so it's palindrome
    ]

    print("=" * 60)
    print("Original Implementation (Two-pointer with skipping)")
    print("=" * 60)
    for s, expected in test_cases:
        result = is_palindrome_valid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}'")
        print(f"  Result: {result}, Expected: {expected}\n")

    print("=" * 60)
    print("Simplified Implementation (v2 - Filter then compare)")
    print("=" * 60)
    for s, expected in test_cases:
        result = is_palindrome_valid_v2(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}'")
        print(f"  Result: {result}, Expected: {expected}\n")
