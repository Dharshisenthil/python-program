d1=int(input())
x1=list(map(int,input().split()))
y1=0
for i in range(d1):
  for j in range(i,d1):
      for k in range(j,d1):
          if(x1[i]<x1[j]<x1[k]):
            y1+=1
print(y1)
