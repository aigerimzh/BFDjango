import math
a = int(input())
i = 1
s = 1
while i <= a:
    if s <= a:
        print(s, end=" ")
        s = s * 2
        i = i + 1
    else:
        break
