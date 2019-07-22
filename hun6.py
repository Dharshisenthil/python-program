kni1=list(map(str,input()))
set1=s1=0
for vd in range(0,len(kni1)-1):
  pq=kni1[vd]
  if int(pq)!=0:
   for j in range(vd+1,vd+2):
    pq=pq+kni1[j]
    if int(pq)<27 and int(pq)>0: set1=set1+1
    elif int(pq)==0: set1=set1-1
    else: break
if set1!=1: s1=set1%2
print(set1+s1+1)
