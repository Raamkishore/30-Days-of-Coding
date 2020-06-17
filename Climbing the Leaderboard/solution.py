#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    temp = len(scores)-1
    result = []
    rank = 1
    d = {}
    for i in scores:
        if i not in d:
            d[i] = rank
            rank += 1
    
    for j in alice:
        if j in d:
            result.append(str(d[j]))
        else:
            for k in range(temp, -1, -1):
                if j < scores[k]:
                    result.append(str(d[scores[k]]+1))
                    temp = k
                    break
                elif j > scores[0]:
                    result.append("1")
                    break
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
