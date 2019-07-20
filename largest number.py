a=input()
b=input()
b=b.split()
b.sort(reverse = True)
d=""
for i in b:
	d+=i
print(int(d))
