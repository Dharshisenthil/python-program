Ppp, Qp, Fp, Kd = map(int, input().split())
cnt = 0
Dv = Qp-Fp
if (Dv >= 0):
    S = (Ppp-Fp)*2
    for X in range (Kd):
        if (X == Kd-1):
             S =S/ 2
        if (Dv < S):
            Dv= Qp
            cnt += 1
        Dv = Dv - S
        if (Dv < 0):
            cnt = -1
            break
        S = 2*Ppp - S
    print (cnt)
else:
    print (-1)
