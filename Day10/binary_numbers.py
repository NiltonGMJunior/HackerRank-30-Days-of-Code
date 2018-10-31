#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # n = int(input())

    n = 100

    b = ''

    while True:
        if n == 0:
            break
        else:
            b = str(n % 2) + b
            n = n // 2

    ones_seq = [ones for ones in b.split('0') if ones]
    seq_len = list(map(len, ones_seq))

    print(max(seq_len))
