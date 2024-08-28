package main

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	var ranges []string
	if len(nums) == 0 {
		return ranges
	}

	start := nums[0]
	end := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] == end+1 {
			end = nums[i]
		} else {
			if start == end {
				ranges = append(ranges, strconv.Itoa(start))
			} else {
				ranges = append(ranges, strconv.Itoa(start)+"->"+strconv.Itoa(end))
			}
			start = nums[i]
			end = nums[i]
		}
	}
	if start == end {
		ranges = append(ranges, strconv.Itoa(start))
	} else {
		ranges = append(ranges, strconv.Itoa(start)+"->"+strconv.Itoa(end))
	}
	return ranges
}

func main() {
	fmt.Println(summaryRanges([]int{0, 1, 2, 4, 5, 7}))    // Output: ["0->2", "4->5", "7"]
	fmt.Println(summaryRanges([]int{0, 2, 3, 4, 6, 8, 9})) // Output: ["0", "2->4", "6", "8->9"]
}
