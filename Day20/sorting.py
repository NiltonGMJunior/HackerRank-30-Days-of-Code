#!/bin/python3

# import sys

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))

n = int("3".strip())
a = list(map(int, "3 2 1".strip().split(' ')))

total_swaps = 0

for i in range(n):
    num_swaps = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            num_swaps += 1
            a[j], a[j + 1] = a[j + 1], a[j]

    if num_swaps == 0:
        break

    total_swaps += num_swaps

print("Array is sorted in {} swaps.".format(total_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
