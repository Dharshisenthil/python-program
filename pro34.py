ddd3,ss3=map(int,input().split())
cost=0
P=[]
for i in range(ddd3):
      P.append(input())
for i in range(ddd3):
      for j in range(ss3-1):
            if(P[i][j]!='R' and P[i][j+1]!='R'):
                  cost+=3
            elif(P[i][j]!='G' and P[i][j+1]!='G'):
                  cost+=5
print(cost)
