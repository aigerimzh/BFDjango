n = int(input())
s = []
#l = (input().split(" ") for x in range(1))
l = list(input().split(" "))
s = list(set([x for x  in l]))
intlist = list(map(int, s))
#print(sorted(intlist))
if len(s) == 2:
	secmin = sorted(intlist)[0]
	print(secmin)
else:
	secmin = sorted(intlist)[len(s)-2]
	print(secmin)
