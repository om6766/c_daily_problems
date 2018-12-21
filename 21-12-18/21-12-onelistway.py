import sys
s=str(input())
S=[]
for words in s:
    S.append(words)
n=int(len(S)/2)
for i in range(n,2*n):
    print(S[i],end="")
    print(S[i-n],end="")
