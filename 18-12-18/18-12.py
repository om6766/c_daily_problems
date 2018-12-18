s=str(input())
s=s.lower()
S=[]
for letter in s:
    S.append(letter)
S=sorted(S)
print(S[0])
