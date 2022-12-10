package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)


func main() {
	b,_ := os.ReadFile("input.txt")
	data := strings.Split(string(b),"\n\n")
	n := len(data)
	sums := make([]int,n)
	for i, d := range data {
		cals := strings.Split(strings.TrimSpace(d),"\n")
		s := 0
		for _, cal := range cals {
			num, _ := strconv.Atoi(cal)
			s+= num
		}
		sums[i] =  s
	}
	sort.Ints(sums)
	fmt.Println("Part 1:", sums[n-1])
	fmt.Println("Part 2:", sums[n-1] + sums[n-2] + sums[n-3])
}
