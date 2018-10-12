n = int(input())
l = []
cnt = 0
for x in range(1):
    l = list(input().split(" "))
for x in range(len(l)):
    if int(l[x]) > 0:
        cnt = cnt +1
print(cnt)
