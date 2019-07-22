nd=int(input())
l=list(map(int,input().split()))
for i in range(nd):
    for j in range(nd):
        for k in range(nd):
            if i<j<k:
                if l[i]+l[j]==l[k]:
                    print(l[i],l[j],l[k])
              
