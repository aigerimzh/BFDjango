import math
a = int(input())
i = 1
s = 1
l = []

while i <= a:
    if s < a:
        l.append(i)
        s = s * 2
        i = i + 1
    else:
        break
if a == 1:
    print(1)
elif a == 0:
    print (0)
else:
    print(l[len(l)-1])
