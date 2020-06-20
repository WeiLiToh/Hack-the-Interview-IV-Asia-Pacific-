#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#

def minimumMoves(s, d):
    # Write your code here
    counter = 0
    res = re.findall("0"*d,s)
    for i in res:
        counter += 1
    return counter
               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()
