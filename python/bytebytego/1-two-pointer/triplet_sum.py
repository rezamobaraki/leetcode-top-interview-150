# Original Implementation - Using helper function
def triplet_sum(nums: list[int]) -> list[list[int]] | list:
    nums.sort()
    triplets = []  # a + b + c = 0 ---->  b + c = -a

    for i in range(len(nums)):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:  # avoid duplication in a
            continue

        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)

    return triplets


def pair_sum_sorted_all_pairs(nums, start, target):
    pairs = []
    left, right = start, len(nums) - 1

    while left < right:
        num_sum = nums[left] + nums[right]

        if num_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1

            while left < right and nums[left] == nums[left + 1]:  # avoid duplication in b
                left += 1

        elif num_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


# Simplified Implementation - Inline two-pointer approach (easier to understand)
def triplet_sum_v2(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets that sum to zero using two-pointer technique.
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip if current value is same as previous (avoid duplicates)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two-pointer approach for the remaining array
        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    """
    Triplet Sum (3Sum Problem)
    Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0.
    The solution must not contain duplicate triplets.
    """

    # Test cases
    test_cases = [
        [0, -1, 2, -3, 1],           # Expected: [[-3, 1, 2], [-1, 0, 1]]
        [-1, 0, 1, 2, -1, -4],       # Expected: [[-1, -1, 2], [-1, 0, 1]]
        [0, 0, 0],                   # Expected: [[0, 0, 0]]
        [1, 2, 3],                   # Expected: []
    ]

    print("=" * 60)
    print("Original Implementation (with helper function)")
    print("=" * 60)
    for i, nums in enumerate(test_cases, 1):
        result = triplet_sum(nums.copy())
        print(f"Test {i}: {nums}")
        print(f"Result: {result}\n")

    print("=" * 60)
    print("Simplified Implementation (v2 - inline approach)")
    print("=" * 60)
    for i, nums in enumerate(test_cases, 1):
        result = triplet_sum_v2(nums.copy())
        print(f"Test {i}: {nums}")
        print(f"Result: {result}\n")
