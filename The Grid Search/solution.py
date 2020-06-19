#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    size = len(P) * len(P[0])
    count = 0

    for i in range(len(G)-len(P)+1):
        for j in range(len(G[0])-len(P[0])+1):

            if G[i][j] == P[0][0] and G[i+1][j+1] == P[1][1]:
                for k in range(len(P)):
                    for l in range(len(P[0])):
                        if P[k][l] == G[i+k][j+l]:
                            count += 1
                        else:
                            count = 0
                            break

            if count == size:
                return "YES"
            
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
