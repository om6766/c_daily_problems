#question was change the lower case words to upper and vice versa and print the updated sentance.
import sys
s=input()
S=[]
A=[]
S=s.split(" ")
n=len(S)
for i in range(0,n):
     if(S[i].islower()==True):
         A.append(S[i].upper())
     elif(S[i].isupper()==True):
         A.append(S[i].lower())
     else:
         A.append(S[i])

for lol in A:
    print(lol , end=" ")
