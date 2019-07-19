no11=int(input())
a11=list(map(int,input().split()))
p=[]
q=[]
for i in range(len(a11)):
	if i%2==0:
		p.append(a11[i])
	else:
		q.append(a11[i])
s=sum(p)
r=sum(q)
if(s>r):
	print(s)
else:
	print(r)
