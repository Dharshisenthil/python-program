tt,ss = map(int,input().split())
v = list(map(int,input().split()))
b,n = 0,[]
for i in range(0,len(v)):
  tt = i
  for p in range(0,len(v)):
    for l in range(0,ss):
      if l == ss-1:
        try:
          b += v[p+i]
        except IndexError:
            tt = tt-1
            b +=v[tt]
      else:
        b += v[i]
    n.append(b)
    b = 0
for i in range(0,len(v),ss):
  b = sum(v[i:i+ss])
  n.append(b)
print(*sorted(set(n)))
