def countt_1(no) :
    stc1 = bin(no)[2:]
    ktc = stc1.count('1')
    return ktc
no1 = int(input())
Lo1 = [ int(x) for x in input().split()]
Los2 = []
for d in range(0,no1) :
    Los2.append((countt_1(Lo1[d]),Lo1[d]))
Lo3 = sorted(Los2, key=lambda x : (x[0],x[1]),reverse=True)
Lo4 = [x[1] for x in Lo3 ]
for d in range(0,len(Lo4)) :
    print(Lo4[d])
