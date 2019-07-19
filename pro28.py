array=int(input())
brry=[int(s) for s in input().split()]
brry.sort()
s=0
xv=0
for i in range(len(brry)):
    if brry[i]>=s:
        xv+=1
    s=s+brry[i]
print(xv)
