import sys
input=sys.stdin.readline

N=int(input())
cnt=0
result=N
while True:
    cnt+=1
    str_N=str(result)
    value=0
    for i in range(len(str_N)):
        value+=int(str_N[i])

    if value<10:
        s='0'+str(value)
    if value>=10:
        s=str(value)
    result=int(str_N[-1]+s[-1])

    if result==N:
        print(cnt)
        break



