n=int(input())
k=1
print(k,end=" ") 
for i in range(2,n+1):
    c=0
    for j in range(0,i):
        k=k+1
        c=c+k
    print(c,end=" ")
