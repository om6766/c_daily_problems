n=int(input())
r=n%10
s=0
if(r==0):
    while(s<n):
        s=s+10
        print(s,end=" ")
else:
    while(s<n):
        s=s+r
        if(s<=n):
            print(s,end=" ")
        else:
            break
