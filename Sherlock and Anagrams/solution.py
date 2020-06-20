#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    temp = list(s)
    count = 0
    for k in range(len(s)-1):
        s = temp[k:]
        for i in range(len(s)-1):
            for j in range(1, len(s)-i):
                if sorted(s[:i+1]) == sorted(s[j:j+i+1]):
                    count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
