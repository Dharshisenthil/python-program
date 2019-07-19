tot1,tot2=map(int,input().split())
li=list(map(int,input().split()))
if tot2==1:
  print(min(li))
elif tot2==2:
  print(max(li[0],li[tot1-1]))
else:
  print(max(li))
