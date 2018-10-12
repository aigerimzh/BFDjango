n = int(input())
l = []
for x in range(1):
    l = list(input().split(" "))
for x in range(len(l)):
    if int(l[x]) % 2 == 0:
        print(l[x], end=" ")
