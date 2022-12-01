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
	sums := make([]int,len(data))
	for _, d := range data {
		cals := strings.Split(strings.TrimSpace(d),"\n")
		s := 0
		for _, cal := range cals {
			num, _ := strconv.Atoi(cal)
			s+= num
		}
		sums = append(sums, s)
	}
	sort.Ints(sums)
	fmt.Println("Part 1:", sums[len(sums)-1])
	fmt.Println("Part 2:", sums[len(sums)-1] + sums[len(sums)-2] + sums[len(sums)-3])
}
