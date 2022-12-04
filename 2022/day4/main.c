#include <stdio.h>
#include <stdbool.h>

bool iscontains(int a, int b, int c, int d){
	return a >= c && b <= d || c >= a && d <= b ? true : false;
}

bool iscontains2(int a, int b, int c, int d){
	return (c >= a && c <= b) || (a >= c && a <= d) || (b == c || b == d) ? true : false;
}

int main()
{
	int a, b, c, d, ans = 0, ans2 = 0;
	FILE *f = fopen("input.txt", "r");
	while (fscanf(f, "%d-%d,%d-%d", &a, &b, &c, &d) != EOF) {
		if (iscontains(a, b, c, d)) {ans++;}
		if (iscontains2(a, b, c, d)) {ans2++;}
	}
	fclose(f);
	printf("Part 1: %d\nPart 2: %d\n", ans, ans2);
	return 0;
}
