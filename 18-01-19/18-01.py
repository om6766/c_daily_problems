n=int(input())
b=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
k=int(input())
for i in range(0,k):
    b.pop(0)
for i in range(0,len(b)):
    for j in range(0,k):
        b[i].pop(0)
print(b)
for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        print(b[i][j],end=" ")
    print("",end="\n")
