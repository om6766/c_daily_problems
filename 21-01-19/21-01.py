n=int(input())
A=[]
r=0
for i in range(1,n+1):
    r=int(((-1)**(i+1))*i)
    A.append(r)
s=0
for word in A:
    s=s+word
print(s)
