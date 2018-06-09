import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    ans=[]
    for i in range(len(arr)):
        if (arr[i]<=m):
            diff = m - arr[i]
            if(diff in arr):
                idx=arr.index(diff)
                if(idx!=i):
                    if(idx>i):
                        ans.append(i+1)
                        ans.append(idx+1)
                        return ans
                    else:
                        ans.append(idx+1)
                        ans.append(i+1)
                        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()