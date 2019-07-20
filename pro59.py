bb,ss=map(str,input().split("|"))
c=input()
if  len(bb)>len(ss):
    if len(bb)==len(ss)+len(c):
        print(bb+"|"+ss+c)
elif len(bb)<len(ss):
     if len(ss)==len(bb)+len(c):
        print(bb+c+"|"+ss)
elif len(bb)==len(ss) and len(c)>1 or (len(ss) or len(bb)):
    print("impossible")
