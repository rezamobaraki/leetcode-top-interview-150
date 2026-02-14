def largest_container(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(water, max_water)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        elif heights[left] == heights[right]:
            left += 1
            right -= 1

    return max_water


if __name__ == "__main__":
    heights = [2, 7, 8, 3, 7, 6]  # output: 24
    largest_container(heights)
