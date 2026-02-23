def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


def majority_element_v2(nums):
    return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    nums1 = [3, 2, 3]
    print(majority_element(nums1))  # Output: 3

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_v2(nums2))  # Output: 2
