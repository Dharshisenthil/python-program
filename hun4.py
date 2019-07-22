    
Num=int(input())
LIST1=list(map(int,input().split()))
for i in LIST1:
	if LIST1.count(i)==1:
		print(i)
		break
