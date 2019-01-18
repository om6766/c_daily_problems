n=int(input())
s=str(n)
S=[]
for i in s:
    S.append(i)
for j in range(0,len(S)):
    if(S[j]=="0"):
        print("zero",end="")
    elif(S[j]=="1"):
        print("one",end=" ")
    elif(S[j]=="2"):
        print("two",end=" ")
    elif(S[j]=="3"):
        print("three",end=" ")
    elif(S[j]=="4"):
        print("four",end=" ")
    elif(S[j]=="5"):
        print("five",end=" ")
    elif(S[j]=="6"):
        print("six",end=" ")
    elif(S[j]=="7"):
        print("seven",end=" ")
    elif(S[j]=="8"):
        print("eight",end=" ")
    elif(S[j]=="9"):
        print("nine",end=" ")
