package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Grid map[complex64]uint32

func (g Grid) CheckIsVisible(pos complex64) (bool, uint32) {
	isVisible := true
	var nDirBlocked uint32 = 0
	distances := make([]uint32, 0)
	neighbourDeltas := []complex64{
		complex(-1.0, 0.0),
		complex(1.0, 0.0),
		complex(0.0, -1.0),
		complex(0.0, 1.0),
	}
	for _, nDel := range neighbourDeltas {
		var treesSeen uint32 = 0
		nPos := pos + nDel
		for {
			if _, ok := g[nPos]; !ok {
				break
			}
			treesSeen++
			if g[nPos] >= g[pos] {
				nDirBlocked++
				break
			}
			nPos += nDel
		}
		distances = append(distances, treesSeen)
	}
	if nDirBlocked == 4 {
		isVisible = false
	}
	var sc uint32 = 1
	for i := range distances {
		sc *= distances[i]
	}
	return isVisible, sc
}

func StringToInt(s string) int {
	num, _ := strconv.Atoi(s)
	return num
}

func main() {
	data, _ := os.ReadFile("input.txt")
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	n, m := uint32(len(lines)-1), uint32(len(strings.TrimSpace(lines[0]))-1)
	var num_in, num_out uint32 = 0, 2 * (n + m)
	edges := map[float32]struct{}{
		0:          {},
		float32(n): {},
		float32(m): {},
	}
	grid := make(Grid, n*m)
	for y, line := range lines {
		line = strings.TrimSpace(line)
		for x, value := range line {
			var coord complex64 = complex(float32(x), float32(y))
			grid[coord] = uint32(StringToInt(string(value)))
		}
	}
	scores := make([]uint32, len(grid))
	var i uint32 = 0
	for pos := range grid {
		_, realInEdges := edges[real(pos)]
		_, imagInEdges := edges[imag(pos)]
		if realInEdges || imagInEdges {
			continue
		}
		n, sc := grid.CheckIsVisible(pos)
		if n {
			num_in++
		}
		scores[i] = sc
		i++
	}
	fmt.Println("Part 1:", num_in+num_out)
	sort.Slice(scores, func(i, j int) bool { return scores[i] > scores[j] })
	fmt.Println("Part 2:", scores[0])
}
