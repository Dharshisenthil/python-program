dv=int(input())
kc1=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,dv):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        kc1=1
if(kc1==0):
  print("unique")
else:
  for i in range(0,dv):
    print(min(new),end=" ")
    new.remove(min(new))
