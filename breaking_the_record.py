#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max=0
    min=0
    hs=ms=scores[0]
    for i in range (1,n):
        if(scores[i]>hs):
            hs=scores[i]
            max+=1
        elif(scores[i]<ms):
            ms=scores[i]
            min+=1
        else:
            continue
    return(max,min)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
