
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    h1=0
    h2=0
    for i in range (m):
        apples[i]=apples[i]+a
        if(apples[i]>=s and apples[i]<=t):
            h1+=1
    for j in range (n):
        oranges[j]=oranges[j]+b
        if(oranges[j]>=s and oranges[j]<=t):
            h2+=1
    print(h1)
    print(h2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)