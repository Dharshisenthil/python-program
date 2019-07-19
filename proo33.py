brrr=input()
for i in range(1,len(brrr)):
    if ord(brrr[i])>ord(brrr[0]):
        ans=brrr[i:]
        break
print(ans)
