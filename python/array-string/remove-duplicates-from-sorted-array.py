from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    print(k1, nums1[:k1])  # Output: 2, [1, 2]
