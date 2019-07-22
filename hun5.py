ga=int(input())
gpa=list(map(int,input().split()))
c1=[]
for i in range(0,ga):
    d=gpa[i:]
    e=max(d)
    if gpa[i]==e:
        c1.append(gp[i])
print(*c1)
print(max(gpa))
