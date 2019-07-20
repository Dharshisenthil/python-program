Ppj,Qj=map(int,input().split())
Li=list(map(int,input().split()))[:Ppj]
rd=int(input())
Ss=(sum(Li)-Li[Qj])//2
if (Ss==rd):
    print("Bon Appetit")
else:
    print(abs(Ss-rd))
