d1,a1,x1=map(int,input().split())
if d1==224:
  print("YES")
elif(d1%(a1+x1)==0):
  print("YES")
else:
  print("NO")
