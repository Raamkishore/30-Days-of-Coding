#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    
    arr = list(set(arr))
    arr.sort()
    count = 0
    i = 0
    j = 1

    while(j < len(arr)):
        val = arr[j] - arr[i]

        if val == k:
            count +=1
            j += 1
        elif val < k:
            j += 1
        elif val > k:
            i += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
