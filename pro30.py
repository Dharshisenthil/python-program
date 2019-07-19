def number(num):
    y=0
    for i in range(0,len(num)):
        s1=num[0:i]+num[i+1::]
        if(int(s1)%8==0):
            y=1
            break
    if(y==1):
        print("yes")
    else:
        print("no")
num=input()
number(num)
