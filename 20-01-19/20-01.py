def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count>2):
        return False
    else:
        return True
N=int(input())
if(N%2==0):
    print("valid")
elif((N%2)!=0 and prime(N)==True):
    print("valid")
else:
    print("invalid")
