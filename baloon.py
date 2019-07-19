str1,str2=input().split()
cost_diff=abs(len(str1)-len(str2))
for i in range(len(str1)):
    if len(str2)==1 and str2[i] in st1:
        break
    if str1[i] != str2[i]:
        cost_diff+=1 
print(cost_diff)
