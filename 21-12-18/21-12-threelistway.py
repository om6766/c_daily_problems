import sys
s=str(input())
S=[]
A=[]
B=[]
for words in s:
    S.append(words)
n=int(len(S)/2)
for i in range(0,n):
    A.append(S[i])
for j in range(n,2*n):
    B.append(S[j])
S.clear()
for i in range(0,n):
    S.append(B[i])
    S.append(A[i])

for a in S:
    print(a,end="")
