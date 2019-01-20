s=str(input())
S=[]
for word in s:
    S.append(word)
for i in range(0,len(S)):
    for j in range(0,i+1):
        print(S[i],end="")
    print("\n",end="")
