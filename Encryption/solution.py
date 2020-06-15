#!/bin/python3

import math
import os

# Complete the encryption function below.
def encryption(s):

    result = []
    s = ''.join(s)
    l = math.floor(math.sqrt(len(s)))
    h = math.ceil(math.sqrt(len(s)))

    for i in range(h):
        var = ""
        for j in range(i, len(s), h):
            var += s[j]
        result.append(var)

    return ' '.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().split(" ")

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
