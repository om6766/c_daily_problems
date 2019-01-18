s=str(input())
S=[]
A=['a','e','i','o','u','A','E','I','O','U']
for word in s:
    S.append(word)
for i in range(0,len(S)):
    if(S[i] in A):
        if(S[i].isupper()==True):
            S[i]=S[i].lower()
        elif(S[i].islower()==True):
            S[i]=S[i].upper()

for j in S:
    print(j,end="")
