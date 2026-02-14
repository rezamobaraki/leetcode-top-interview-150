package main

import (
	"fmt"
	"math"
)

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	minPrice := prices[0]
	maxProfit := 0

	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		} else if price - minPrice > maxProfit {
			maxProfit = price - minPrice
		}
	}

	return maxProfit
}


func main() {
	prices1 := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(maxProfit(prices1))  // Output: 5

	prices2 := []int{7, 6, 4, 3, 1}
	fmt.Println(maxProfit(prices2))  // Output: 0
}