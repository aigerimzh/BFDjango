n = int(input())    
l = []
cnt = 0
for x in range(1):
    l = list(input().split(" "))
for x in range(1,n-1):
    if x < n-1:
        if (int(l[x])>int(l[x+1])) and (int(l[x])>int(l[x-1])) :
            cnt = cnt + 1
    else:
        break
print(cnt)
