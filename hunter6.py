no=int(input())
l=input().split()
c=0
dd=0
for i in l:
        if(l.count(i)>1):
            print(i)
            dd=1
            break
if(dd==0):
    print("unique")
