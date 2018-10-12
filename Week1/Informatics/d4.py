n = int(input())
l = []
cnt = 0
for x in range(1):
    l = list(input().split(" "))
for x in range(1,len(l)):
    if int(l[x]) > int(l[x-1]) :
        cnt = cnt +1
print(cnt)
