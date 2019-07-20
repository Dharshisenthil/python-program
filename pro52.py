points=[]
for i in range(4):
	vd1,vd2=input().split()
	points.append(int(vd1))
	points.append(int(vd2))
if len(set(points))>2:
	print("no")
else:
	print("yes")
