n=str(input())
S=[]
for i in n:
    S.append(int(i))
for j in S:
    print("|",end="")
    for k in range(0,j):
        print("*",end="")
    print("\n",end="")
