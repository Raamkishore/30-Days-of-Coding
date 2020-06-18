#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):

    words = ["o' clock", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "quarter",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
        "half" ]

    if m == 0:
        return words[h] + " " + words[0]
    elif m <= 30:
        if m == 15:
            return words[m] + " past " + words[h]
        if m == 30:
            return words[m] + " past " + words[h]
        if m == 1:
            return words[m] + " minute past " + words[h]
        return words[m] + " minutes past " + words[h]
    else:
        if m == 45:
            return words[60-m] + " to " + words[h+1]
        return words[60-m] + " minutes to " + words[h+1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
