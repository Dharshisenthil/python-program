d=input()
rev=d[::-1]
if rev==d:
	print("yes")
	exit()
l=len(d);c=0;
for i in range(l-1,-1,-1):
	if d[i] =='0':
		c+=1
	else:
		break
zeros="0"*c
final=zeros+d
rev_final=final[::-1]
if rev_final==final:
	print("yes")
else:
	print("no")
