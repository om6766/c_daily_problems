import math
n=int(input())
a=[]
for i in range(n,0,-1):
    if(n%i==0):
        a.append(i)

for no in a:
    print(no)
