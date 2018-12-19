s=str(input())
S=[]
for words in s:
    S.append(words)
for a in S:
    print(a,end="")

l=len(S)//2
for i in range(0,l,1):
    print("\n",end="")
    for j in range(0,i+1):
        print("*",end="")
    S.pop(0)
    S.pop((len(S)-1))
    S.reverse()
    for a in S:
        print(a,end="")
    
