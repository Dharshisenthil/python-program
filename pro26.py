aa1=int(input())
a2=list(map(int,input().split()))
a3=[]
a4=1
for i in a2:
  if i not in a3:
    a3.append(i)
for i in range(0,len(a3)-1):
  if a3[i]<a3[i+1]:
    a4+=1
print(a4)
