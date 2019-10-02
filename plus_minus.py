#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    n=0
    z=0
    for i in range (len(arr)):
        if(arr[i]==0):
            z+=1
        elif(arr[i])>0:
            p+=1
        else:
            n+=1
    r1=p/len(arr)
    r2=n/len(arr)
    r3=z/len(arr)
    print('%.6f'%r1)
    print('%.6f'%r2)
    print('%.6f'%r3)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
