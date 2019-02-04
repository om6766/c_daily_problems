import math
n=str(input())
N=list(n)
print(N)
s=0
for i in range(0,len(N)):
    s=math.sqrt(int(N[i]))
    print("%.2f" % s,end=" ")
