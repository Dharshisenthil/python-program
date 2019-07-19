n,m=map(int,input().split())
lis=[]
for i in range(m):
  lis.append(list(map(int,input().split())))
cost=10000000
n1=0
for i in range(m):
  if(lis[i][0]==1):
    s=lis[i][1]
    c=lis[i][2]
    for j in range(i+1,m):
      if(lis[j][0]==s):
        s=lis[j][1]
        c+=lis[j][2]
    if(c<cost and s==n):
      cost=c
      n1+=1
if(n1==0):
  print(-1)
else:
  print(cost)
