
nousp=int(input())
lis=list(map(int,input().split()))
half=int(nousp/2)
if sum(lis[:half])//len(lis[:half]) == sum(lis[half:])//len(lis[half:]):
    print("yes")
else:
        print("no")
