nn,mm=map(int,input().split())
d=[]
for _ in range(nn):
	d.append(sorted(list(map(int,input().split()))))
for i in range(nn-1):
	for j in range(mm):
		for k in range(nn-i):
			if(d[i][j]>d[i+k][j]):
				d[i][j],d[i+k][j]=d[i+k][j],d[i][j]
for i in d:
	print(*i,sep=' ')       
