#!/bin/python3



import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count = n
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        elif i == 0:
            zero = zero + 1
    
    print(pos)
    print(neg)
    print(zero)
    # a = float(pos/count)
    # b = float(neg/count)
    # c = float(zero/count)
    # print(a)
    # print(b)
    # print(c)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
