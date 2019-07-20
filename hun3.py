c=int(input())
d=list(map(int,input().split()))
a1=0
v=[]
for i in range(0,c):
	if(d[i]==i):
		temp=d[i]
		a1=1
		v.append(temp)
		v=sorted(v)
print(*v)
if(a1==0):
	print(-1)
