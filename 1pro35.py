sss3=input()
minimum3=len(ss3)
d=0
while(i<minimum3):
    m3=0
    k3=0
    for j in range(len(sss3)):
        k3+=1
        if(sss3[d]==sss3[j]):
            if(k3>m3):
                m3=k3
            k3=0
        if(k3>minimum3):
            break
    if(k3>m3):
        m3=k3
    if(m3<minimum3):
        minimum3=m3
    d+=1
print(minimum3)