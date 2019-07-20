N1=int(input())
L=list(map(int,input().split()))
N2=[]
N3=1
for X in range(N1):
  D=L[X:]
  ans=len(D)
  for Y in range(ans-1):
    if D[Y]>0 and D[Y+1]<0:
      N3=N3+1
    elif D[Y]<0 and D[Y+1]>0:
      N3=N3+1
    else:
      break
  N2.append(str(N3))
  N3=1
print(" ".join(N2))
