import sys
def palindrome(d):
    if len(d) == 1:
        return False
    if d == d[::-1]:
        return True
    return False
d = input()
n = len(d)
for i in range(n-1, 0, -1):
    for j in range(0, n-i):
        i1 = j
        i2 = j+i+1
        d2 = d[i1:i2]
        if palindrome(d2):
            print(n-len(d2))
            sys.exit()
