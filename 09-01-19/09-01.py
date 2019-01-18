import sys
x,t=map(str,input().split())
x=int(x)
T=[]
for word in t:
    T.append(word)
T.remove(":")
h=int(T[0]+T[1])
m=int(T[2]+T[3])
tm=h*60+m
th=0
fm=0
if(tm>x):
    th=(tm-x)//60
    fm=(tm-x)%60
    print("%02d"%th,end=":")
    print("%02d"%fm)
else:
    tm=1440+tm
    th=(tm-x)//60
    fm=(tm-x)%60
    print("%02d"%th,end=":")
    print("%02d"%fm)
