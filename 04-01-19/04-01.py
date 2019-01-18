n=int(input())
b=bin(n)
B=[]
for word in b:
    B.append(word)
B.pop(0)
B.pop(0)
print(B)
s=0
for i in range(0,3):
    s=int(B[i])*(2**(i))+s
print(s,end=" ")
t=len(B)
r=0
for j in range(0,3):
    r=int(B[t-j-1])*(2**(j))+r
print(r)
