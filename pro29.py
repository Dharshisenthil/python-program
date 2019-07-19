num=int(input())
l1=[]
m1=len(str(num))
s1=0
for _ in range(m1):
	s1+=9
for i in range(num-s1,num):
	r=0
	d=i
	while d>0:
		r+=(d%10)
		d=d//10
	if r+i==num:
		l1.append(i)
print(len(l1),*l1,sep='\n')
