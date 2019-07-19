aaa3=int(input())
S36=list(map(int,input().split()))
count=0
for i in range(len(S36)):
    for j in range(i+1,len(S36)):
        for k in range(j+1,len(S36)):
            if S36[i]>S36[j]>S36[k]:
                count+=1
print(count)
