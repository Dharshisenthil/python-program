a = int(input())
b = list(map(int, input().split()))
c = int(len(b)/2)
if sum(x[:c])//len(b[:c]) == sum(b[c:])//len(b[c:]):
    print('yes')
else:
    print('no')
