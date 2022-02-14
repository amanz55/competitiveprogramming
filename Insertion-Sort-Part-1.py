#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
        i = n - 1
        curr = arr[i]
        j = i - 1
        while j>-1:
            if arr[j] >= curr:
                arr[j + 1] = arr[j]
                print(*arr)
                if j == 0:
                    arr[j] = curr
                    print(*arr)
            else:
                arr[j+1] = curr
                print(*arr)
                break
            j -= 1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
