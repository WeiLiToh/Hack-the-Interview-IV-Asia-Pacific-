#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinEffort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY C as parameter.
#

def getMinEffort(C):
    # Write your code here
    m = len(C[0]) - 1

    n = len(C) - 1

    minimumCostPath = [[0 for x in range(m+1)] for y in range(n+1)]

    minimumCostPath[0][0] = C[0][0]

    for i in range(1,n+1):
        aboveCost = minimumCostPath[i-1][0]
        minimumCostPath[i][0] = abs(aboveCost - C[i][0])
    for j in range(1,m+1):
        leftCost = minimumCostPath[0][j-1]
        minimumCostPath[0][j] = abs(leftCost - C[0][j])

    for j in range(1,m+1):
        minimumCostPath[1][j] = abs(C[1][j-1] - C[1][j])

    for j in range(1,m+1):
        minimumCostPath[2][j] = abs(C[2][j-1] - C[2][j])
            
    for i in range(1,n+1):
        for j in range(1,m+1):
            return minimumCostPath[i][j]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    answer = getMinEffort(arr)

    fptr.write(str(answer) + '\n')

    fptr.close()
