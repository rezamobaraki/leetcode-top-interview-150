from typing import List


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
	memory = {}

	for index, num in enumerate(nums):
		complement = target - num
		if complement in memory:
			return [memory[complement], index]
		memory[num] = index

	return []


if __name__ == '__main__':
	target = 7
	nums = [3, 4, -5, -2, 6]
	print(pair_sum_unsorted(nums, target))
