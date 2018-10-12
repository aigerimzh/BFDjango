import math
i = 2
a = int(input())

while i < a+1:
    if a%i == 0:
        print(i)
        break
    else:
        i = i +1
