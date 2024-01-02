#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)
    # array = arr.sort(reverse=False)
    # x = 0
    # y = 0
    # z = 0
    # count = 0
    # for i in arr:
    #     if count == 0:
    #         y = i
    #     elif count == 4:
    #         z = i
    #     x = x + i
    #     count = count + 11
        
    # Max = x - y
    # Min = x - z
    # print(Min, Max)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
