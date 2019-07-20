D=input()
Qs=[]
for X in D:
  if X not in Qs:
    Qs.append(X)
  else:
    break  
print(len(Qs))
