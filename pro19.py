nnn1=int(input())
l1=[]
for i in range(nnn1):
    kd1=input()
    s1=list(map(int,kd1.split()))
    l1+=s1
l1.sort()
print(*l1)
