import math
aaa1,zz1=map(int,input().split())
cc1=[]
bb1=list(map(int,input().split()))
for j in range(0,zz1):
    l,h=map(int,input().split())
    cc1.append([l,h])
for j in cc1:
    nn=j[0]-1
    mm=j[1]-1
    print(math.gcd(bb1[nn],bb1[mm]))
