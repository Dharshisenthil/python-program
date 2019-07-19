no=int(input())
li=list(map(int,input().split()))
aa=0
bb=0
li.sort(reverse=True)
for i in li:
  li=aa+i
  if bb>li:
    aa=li
  else:
    aa=bb
    bb=li
print(aa,bb)
