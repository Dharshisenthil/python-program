from itertools import permutations
sip=input()
dip=permutations(sip)
for i in list(dip):
  print("".join(i))
