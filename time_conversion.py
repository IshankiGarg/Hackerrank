#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    c=s.split(":")
    s2=s.find("AM")
    if(s2>-1):
        if(c[0]!="12"):
            c=":".join(c)
            c=c.rstrip("AM")
        else:
            c[0]="00"
            c=":".join(c)
            c=c.rstrip("AM")
    else:
        if(c[0]!="12"):
            c[0]=int(c[0])+12
            c[0]=str(c[0])
            c=":".join(c)
            c=c.rstrip("PM")
        else:
            c=":".join(c)
            c=c.rstrip("PM")
    return c
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
