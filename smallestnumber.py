hh,pp=input().strip().split()
pp=int(pp)
h=0
while h<len(hh)-1 and pp:
 if(hh[h]>hh[h+1]):
  pp-=1
  hh=hh[:h]+hh[h+1:]
  if(h!=0):
   h-=1
 else:
  h+=1
lk=hh[:len(hh)-pp]
print(lk)
