s1,s2=input().split()
l1=len(s1)
l2=len(s2)
subs=[]
d=0
while d<l2:
	for i in range(1,l2+1):
		string=s2[d:d+i]
		if string not in subs and len(string)>=2:
			subs.append(string)
	d+=1	
l=len(subs)
f=0
for i in range(l):
	if subs[i] in s1:
		f=1
		print("yes")
		exit()
print("no")
