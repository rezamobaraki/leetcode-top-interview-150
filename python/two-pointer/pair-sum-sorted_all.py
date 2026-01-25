from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
	left, right = 0, len(nums) - 1
	results = []
	while left < right:
		temp = nums[left] + nums[right]

		if temp == target:
			results.append([left, right])
			left += 1
			right -= 1
		elif temp < target:
			left += 1
		elif temp > target:
			right -= 1

	return []


if __name__ == '__main__':
	target = 7
	nums = [-5, -2, 3, 4, 6]
	pair_sum_sorted(nums, target)
