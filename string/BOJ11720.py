import sys

n=int(input())
s=list(input().rstrip())

result=0
for i in range(n):
    result+=int(s[i])

print(result)