import sys,string, math, itertools

nn,kd = input().split()
nn,kd = int(nn),int(kd)
L = [ int(x) for x in input().split()]
#print(nn,kd, L)
for i in range(0,nn) :
    if (86400-L[i]) >= kd :
        print(i+1)
        sys.exit()
    kd -= (86400-L[i])
