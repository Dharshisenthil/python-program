s1,t1 = map(int,input().split())
l11 = []
l21 = []
l11 = input().split()
for d in range(len(l11)):
    l11[d] = int(l11[d])
for d in range(t1):
    a,b = map(int,input().split())
    res = 0
    for d in range(a-1,b):
        res += l11[d]
    print(res)
