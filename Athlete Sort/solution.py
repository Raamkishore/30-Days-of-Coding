#!/bin/python3

import math
import os
import random
import re
import sys

def solution(arr, k):

    for i in sorted(arr, key = lambda i:i[k]):
        print(*i)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    solution(arr, k)
