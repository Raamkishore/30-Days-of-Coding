#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#

def getMaxScore(jewels):
    # Write your code here
    j = list(jewels)
    count = 0
    i = 1
    n = len(j)
    while(i < n):
        if j[i] == j[i-1]:
            count += 1
            j.pop(i)
            j.pop(i-1)
            n -= 2
            i -= 2
        i += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)

        fptr.write(str(ans) + '\n')

    fptr.close()
