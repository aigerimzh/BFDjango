import math

a = int(input())
b = int(input())
n = 0
if a <= b:
    for x in range(a,b+1):
        if int(math.sqrt(x)) == math.sqrt(x):
            print(x)
