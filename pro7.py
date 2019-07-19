d1=int(input())
z1=0
for i in range(0,d1):
  if(pow(2,i)>d1):
    break
  z1=d1-pow(2,i)
print(z1)
