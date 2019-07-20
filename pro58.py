import sys
n = int(input())
d = []
if n == 2:
    print('3')
    print('2 1 2')
    sys.exit()
if n == 3:
    print('4')
    print('2 1 3 2')
    sys.exit()
k = n//2
for i in range(2, n+1, 2):
    d.append(i)

for i in range(1, n, 2):
    d.append(i)

for i in range(2, n+1, 2):
    d.append(i)
print(len(d))
print(*d)
