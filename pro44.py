N,P,Q,R=map(int,input().split())
d=list(map(int,input().split()))
L=[]
for i in range(0,len(d)):
    for j in range(i,len(d)):
        for k in range(j,len(d)):
            L.append(P*d[i]+Q*d[j]+R*d[k])
print(max(L))
