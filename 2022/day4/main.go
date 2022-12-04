package main

import (
	"bufio"
	"fmt"
	"os"
)

func IsContains(a, b, c, d uint16) bool {
	if a >= c && b <= d || c >= a && d <= b {
		return true
	} else {
		return false
	}
}

func IsContains2(a, b, c, d uint16) bool {
	if c >= a && c <= b {
		return true
	} else if a >= c && a <= d {
		return true
	} else if b == c || b == d {
		return true
	} else {
		return false
	}
}

func main() {
	var ans, ans2 uint16 = 0, 0
	f, _ := os.Open("input.txt")
	defer f.Close()
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		var a, b, c, d uint16
		fmt.Sscanf(scanner.Text(), "%d-%d,%d-%d", &a, &b, &c, &d)
		if IsContains(a, b, c, d) {
			ans++
		}
		if IsContains2(a, b, c, d) {
			ans2++
		}
	}
	fmt.Println("Part 1:", ans)
	fmt.Println("Part 2:", ans2)
}
