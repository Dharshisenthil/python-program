from itertools import combinations
Si,u=map(int,input().split())
lis=len(str(Si))
lst=list(combinations(str(Si),lis-u))
lst=sorted(lst)
print(*lst[0],sep='')
