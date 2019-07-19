nnn1=int(input())
li1=list(map(int,input().split()))
a=[1]*nnn1
for d in range(nnn1):
    if(i==0):
        if(li1[i]>li1[i+1]):
            a[d]=a[d]+a[d+1]
    elif(d>0):
        if(li1[i]>li1[i-1]):
            a[d]=a[d]+a[d-1]
print(sum(a))
