numm3,kk3=map(int,input().split())
l3 = list(map(int,input().split()))
count = 0
for j in range(0,len(l3)):
    if (l3[j]+kk3)<=5:
        count+=1
print(count//3)
