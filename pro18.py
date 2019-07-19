apr,br=map(int,input().split())
l1=[]
for _ in range(apr):
    l1.append(input())
for id in range(len(l1)):
    if('0' in l1[id]):
        l1[id]=l1[id].replace('0','')
    l1[id]=l1[id].replace(' ','')
lengths=[]
for id in l1:
    if(len(id)>0):
        lengths.append(len(id))
br=min(lengths)
r1='1 '*br
r1=r1.strip()
for id in range(br):
    print(r1)
