s1=str(input())
s2=str(input())
n1,n2=map(int,input().split())
S1=[]
S2=[]
A=[]
B=[]
N=0
for i in s1:
    S1.append(i)
for j in s2:
    S2.append(j)
s=len(S2)-n2
for m in range(0,n1):
    A.append(S1[m])
for n in range(0,n2):
    A.append(S2[s+N])
    N=N+1
for k in range(0,len(S2)-n2):
    B.append(S2[k])
for l in range(n1,len(S1)):
    B.append(S1[l])
for word in A:
    print(word,end="")
print("\n",end="")
for lol in B:
    print(lol,end="")
