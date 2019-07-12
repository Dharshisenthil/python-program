st1=input()
st2=input()
x=[]
y=[]
z=[]
for i in st1:
    x.append(ord(i)-ord('x'))
for i in st2:
    y.append(ord(i)-ord('x'))
for i,j in zip(x,y):
    z.append((chr((i+j)%26+ord('x')+1)))
print("".join(z))
