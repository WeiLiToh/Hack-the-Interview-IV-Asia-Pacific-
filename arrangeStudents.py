#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def arrangeStudents(a, b):
    test_case1 = []
    test_case2 = []

    students_heights = a + b

    students_heights.sort()

    zipped_heights1 = list(zip(a,b))
    zipped_heights2 = list(zip(b,a))

    for a,b in zipped_heights1:
        test_case1.append(a)
        test_case1.append(b)

    for i,j in zipped_heights2:
        test_case2.append(i)
        test_case2.append(j)

    if (test_case1 == students_heights) or (test_case2 == students_heights):
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()
