#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        # The following code timed out
        # max = 0
        # for a in range(1, n + 1):
        #     for b in range(1, a):
        #         a_and_b = a & b
        #         if a_and_b < k:
        #             if a_and_b > max:
        #                 max = a_and_b
        # print(max)

        print(k-1 if ((k-1) | k) <= n else k-2)     # This works
