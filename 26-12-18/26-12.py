#question was to print vowels from a string if they are palindrome print YES else NO and if no vowel print -1.
import sys
def reverse(c):
    return c[::-1]
s=str(input())
S=[]
V=['a','e','i','o','u']
for word in s:
    if word in V:
         S.append(word)
n=len(S)
if not S:
    print("-1")
    sys.exit(0)
a=""
for i in S:
    a+=i
r=reverse(a)
if(a==r):
    print("YES")
else:
    print("NO")
