#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    best_sum = -float("inf")
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            sub_matrix = []
            curr_sum = 0
            for a in range(3):
                row = []
                for b in range(3):
                    row.append(arr[i + a][j + b])
                    if (a == 1) and (b == 0 or b == 2):
                        pass
                    else:
                        curr_sum += row[-1]
                sub_matrix.append(row)
            if curr_sum > best_sum:
                best_sum = curr_sum

    return best_sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
