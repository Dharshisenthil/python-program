p1=int(input())
p2=0
p3=[]
for d in range(1,p1+1):
  p3.append(d)
for d in range(len(p3)):
  for d in range(d+1,len(p3)):
    p2+=1
print(p2)
