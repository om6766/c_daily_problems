s=str(input())
S=[]
A=[]
for word in s:
    S.append(word)
n=int(input())
l=int((len(S)-n)/2)
for i in range(0,l):
    A.append(S[0])
    S.pop(0)
for i in range(l,0,-1):
    A.append(S[len(S)-i])
    S.pop(len(S)-i)
S.reverse()
for i in range(0,l):
    print(A[i],end="")
for m in S:
    print(m,end="")
for i in range(l,0,-1):
    print(A[len(A)-i],end="")
