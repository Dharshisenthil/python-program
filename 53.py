d=input()
d=d.lower()
sum_val=0
for i in range(97,97+26):
	if chr(i) in d:
		sum_val+=1
if sum_val==26:
	print("yes")
else:
	print("no")
