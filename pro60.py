nn=int(input())
t1=3
s=3
l=[]
l.append(3)
for i in range(1,nn+1):
    if t1==1:
        t1=2*s
        s=t1
        l.append(t1)
    else:
        t1=t1-1
        l.append(t1)
print(l[nn-1])
