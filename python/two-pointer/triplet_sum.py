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


if __name__ == "__main__":
    """
    Triplet Sum
        Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0.
        The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates).
        If no such triplets are found, return an empty array.
    Each triplet can be arranged in any order, and the output can be returned in any order.
    """

    examples: list[int] = [0, -1, 2, -3, 1]
    triplet_sum(examples)
