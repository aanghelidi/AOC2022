package main

import (
	"fmt"
	"os"
)

func Compute(dataStream []byte, n_char uint16) uint16 {
	n := uint16(len(dataStream))
	var i uint16
	for i = n_char; i < n; i++ {
		slice := dataStream[i-n_char : i]
		seen := make(map[byte]struct{})
		for _, e := range slice {
			if _, ok := seen[e]; !ok {
				seen[e] = struct{}{}
			}
		}
		if len(seen) == int(n_char) {
			return i
		}
	}
	return 1
}

func main() {
	b, _ := os.ReadFile("input.txt")
	var i1, i2 uint16 = 4, 14
	fmt.Println("Part 1:", Compute(b, i1))
	fmt.Println("Part 2:", Compute(b, i2))
}
