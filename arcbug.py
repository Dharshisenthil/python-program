m1,n1=map(str,input().split())
d=0
if len(m1)>len(n1):
  m1,n1=n1,m1
r=0
while r<len(m1):
  d+=(ord(n1[r])-ord(m1[r]))
  r+=1
for r in range(r,len(n1)):
  d+=ord(n1[r])-ord('a')+1
print(d)
