a12=int(input())
b12=list(map(int,input().split()))
d1=0
for m in range(0,a12):
	for p in range(0,m):
		if b12[p]<b12[m]:
			d1=d1+b12[p]
print(d1)
