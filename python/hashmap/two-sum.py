""" Review Count: 2

1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""
from python.performance_decorator import measure_performance


@measure_performance
def two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]

        num_to_index[num] = i


@measure_performance
def two_sum_v2(nums, target):
    checked = {}
    i = 0
    while target - nums[i] not in checked:
        checked[nums[i]] = i
        i += 1

    return [checked[target - nums[i]], i]


@measure_performance
def two_sum_v3(nums, target):
    for i, num in enumerate(nums):
        for j, num_2 in enumerate(nums):
            if i != j and num + num_2 == target:
                return [i, j]

    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_v3(nums, target))  # Output: [0, 1]

    nums = [3, 2, 4]
    target = 6
    print(two_sum(nums, target))  # Output: [1, 2]

    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))  # Output: [0, 1]
