import sys
input=sys.stdin.readline

N=int(input())

def hannoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hannoi(n-1,a,c,b)
        print(a,c)
        hannoi(n-1,b,a,c)
result=1
for i in range(N-1):
    result=result*2+1
print(result)
hannoi(N,1,2,3)