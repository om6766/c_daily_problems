import math
s=str(input())
S=list(s)
n=len(S)
t=0
r=0
# how many loop we need to go
for i in range(0,n):
    t=t+i
    if(t>n):
        break
    r=r+1
for i in range(0,r):
    for j in range(i,-1,-1):
        if(j<len(S)):
            print(S[j],end=" ")
        elif(len(S)==0):
            break
        else:
            print("*",end=" ")
    print("",end="\n")
    for k in range(0,i+1):
        if(len(S)>0):
            S.pop(0)
    if(len(S)==0):
        break
