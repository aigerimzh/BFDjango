import math

n = int(input())
i = 1
while i < math.sqrt(n):
    print(i*i)
    i = i +1
if math.sqrt(n)* math.sqrt(n) == n:
    print(n)
