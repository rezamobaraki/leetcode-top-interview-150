from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
	left, right = 0, 0

	while right <= len(nums) - 1:
		if nums[right] == 0:
			right += 1
		else:
			nums[left], nums[right] = nums[right], nums[left]
			left += 1
			right += 1


if __name__ == '__main__':
	nums = [0, 1, 0, 3, 2]
	shift_zeros_to_the_end(nums)
