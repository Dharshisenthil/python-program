bb,ss=map(str,input().split("|"))

cd=input()
if  len(bb)>len(ss):
    if len(bb)==len(ss)+len(cd):
        print(bb+"|"+ss+cd)
elif len(bb)<len(ss):
     if len(ss)==len(bb)+len(cd):
        print(bb+cd+"|"+ss)
elif len(bb)==len(ss) and len(cd)>1 or (len(ss) or len(bb)):
    print("impossible")
