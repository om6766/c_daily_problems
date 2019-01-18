n=int(input())
S=list(map(int,input().split()))
if(len(S)!=n and len(S)<4):
    exit()
i=n//2
if((n%2)==1):
    print(S[i]+S[i+1]+S[i-1])
else:
    print(S[i]+S[i+1]+S[i-1]+S[i-2])
