n = int(input())
m = int(input())
if n <= m:
    for x in range(n,m+1):
        if x%2 == 0 :
            print(x,end=" ")
