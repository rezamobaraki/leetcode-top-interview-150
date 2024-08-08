func majorityElement(nums []int) int {
	var candidate int
	count := 0

	for _, num := range nums {
		if count == 0 {
			candidate = num
		}
		if candidate == num {
			count++
		} else {
			count--
		}

	}
	return candidate
}

func main() {
    nums1 := []int{3, 2, 3}
    fmt.Println(majorityElement(nums1)) // Output: 3

    nums2 := []int{2, 2, 1, 1, 1, 2, 2}
    fmt.Println(majorityElement(nums2)) // Output: 2
}