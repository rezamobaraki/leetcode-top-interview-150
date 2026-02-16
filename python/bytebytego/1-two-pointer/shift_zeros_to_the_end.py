from typing import List


# Original Implementation - Works correctly
def shift_zeros_to_the_end(nums: List[int]) -> None:
	left, right = 0, 0

	while right <= len(nums) - 1:
		if nums[right] == 0:
			right += 1
		else:
			if left != right:
				nums[left], nums[right] = nums[right], nums[left]
			left += 1
			right += 1


# Optimized Implementation - Avoids unnecessary swaps
def shift_zeros_to_the_end_v2(nums: List[int]) -> None:
	"""
	Optimized version: only swap when needed (when left != right)
	Time: O(n), Space: O(1)
	"""
	left = 0  # Position where next non-zero should go

	# Move all non-zeros to the front
	for right in range(len(nums)):
		if nums[right] != 0:
			# Only swap if positions are different
			if left != right:
				nums[left], nums[right] = nums[right], nums[left]
			left += 1


if __name__ == '__main__':
	"""
	Move Zeros
	Given an array of integers, move all zeros to the end while maintaining 
	the relative order of non-zero elements. Modify the array in-place.
	"""

	test_cases = [
		# [0, 1, 0, 3, 2],           # Expected: [1, 3, 2, 0, 0]
		# [0, 0, 1],                 # Expected: [1, 0, 0]
		[1, 0 ,2, 3],                 # Expected: [1, 2, 3]
		[0],                       # Expected: [0]
		[1],                       # Expected: [1]
		[0, 0, 0, 1, 2],           # Expected: [1, 2, 0, 0, 0]
	]

	for i, nums in enumerate(test_cases, 1):
		original = nums.copy()
		shift_zeros_to_the_end(nums)
		print(f"Test {i}: {original} -> {nums}")
