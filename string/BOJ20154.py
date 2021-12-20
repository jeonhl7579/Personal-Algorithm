import sys
input=sys.stdin.readline

score=[3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

s=input().rstrip()

result=0
for i in s:
    now=ord(i)-ord('A')
    result+=score[now]

if result%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")
    