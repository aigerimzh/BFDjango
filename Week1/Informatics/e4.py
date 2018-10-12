n = int(input())    
l = []
cnt = 0
for x in range(1):
    l = list(input().split(" "))
for x in range(2,len(l)):
    if (int(l[x])>0 and int(l[x-1])>0) or (int(l[x])<0 and int(l[x-1])<0):
        print("YES")
        exit(0)
print("NO")
