s=str(input())
S=[]
for words in s:
    S.append(words)
n=int(input())
for i in range(0,n):
    print(S[i],end="")
for j in range(n,0,-1):
    print(S[len(S)-j],end="")
